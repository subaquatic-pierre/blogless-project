from abc import ABC, abstractmethod
import json
import boto3

s3 = boto3.resource("s3")


class BaseBucketProxy(ABC):
    def __init__(self, bucket_name, root_dir) -> None:
        self.bucket_name = bucket_name
        self.root_dir = root_dir
        self.bucket_interface = s3.Bucket(bucket_name)

    @abstractmethod
    def get_json(self, filename):
        pass

    @abstractmethod
    def save_json(self, filename):
        pass


class BucketProxy(BaseBucketProxy):
    def get_json(self, object_key):
        object = s3.Object(self.bucket_name, f"{self.root_dir}{object_key}")
        object_res = object.get()
        object_json = json.loads(object_res["Body"].read())
        return object_json

    def save_json(self, body: dict, filename: str):
        self.bucket_interface.put_object(Key=self.root_dir)
        self.bucket_interface.put_object(
            Key=f"{self.root_dir}{filename}",
            Body=json.dumps(body),
        )

    def delete_files(self, filenames):
        if len(filenames) > 0:
            objects = [{"Key": filename} for filename in filenames]
            self.bucket_interface.delete_objects(Delete={"Objects": objects})

    def list_dir(self, dir: str = ""):
        object_summary_iterator = self.bucket_interface.objects.all()
        object_keys = [
            obj.key
            for obj in object_summary_iterator
            if obj.key.startswith(f"{self.root_dir}{dir}")
            and obj.key != f"{self.root_dir}{dir}"
        ]
        return object_keys

    def save_bytes(self, body: bytes, filename: str):
        self.bucket_interface.put_object(
            Key=f"{self.root_dir}{filename}",
            Body=body,
        )