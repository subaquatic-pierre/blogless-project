from unittest.mock import MagicMock
import json
import boto3


class BucketProxy:
    def __init__(
        self, bucket_name, root_dir, test_bucket=False, mock_config={}
    ) -> None:
        self.bucket_name = bucket_name
        self.root_dir = root_dir
        self.test_bucket = test_bucket

        if test_bucket:
            self.bucket_interface = MagicMock()
        else:
            self.bucket_interface = boto3.resource("s3").Bucket(bucket_name)

    def _configure_s3_object(self, object_key):
        if self.test_bucket:
            return MagicMock()
        else:
            return boto3.resource("s3").Object(
                self.bucket_name, f"{self.root_dir}{object_key}"
            )

    def get_json(self, object_key):
        object = self._configure_s3_object(object_key)
        object_res = object.get()

        if self.test_bucket:
            return {}

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
