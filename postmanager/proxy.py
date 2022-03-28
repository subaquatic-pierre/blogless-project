from abc import ABC, abstractmethod
from unittest.mock import MagicMock
import json
import boto3

from exception import BucketProxyException


class BucketProxyBase(ABC):
    def __init__(self, bucket_name, root_dir) -> None:
        self.bucket_name = bucket_name
        self.root_dir = root_dir

    def get_json(self, object_key):
        try:
            object = self._configure_s3_object(object_key)
            object_res = object.get()

            object_json = json.loads(object_res["Body"].read())
            return object_json
        except Exception as e:
            raise BucketProxyException(f"Error fething JSON from bucket, {str(e)}")

    def save_json(self, body: dict, filename: str):
        try:
            self.bucket_interface.put_object(Key=self.root_dir)
            self.bucket_interface.put_object(
                Key=f"{self.root_dir}{filename}",
                Body=json.dumps(body),
            )
        except Exception as e:
            raise BucketProxyException(f"Error saving JSON to bucket, {str(e)}")

    def delete_files(self, filenames):
        try:
            if len(filenames) > 0:
                objects = [{"Key": filename} for filename in filenames]
                self.bucket_interface.delete_objects(Delete={"Objects": objects})
        except Exception as e:
            raise BucketProxyException(f"Error deleting files from bucket, {str(e)}")

    def list_dir(self, dir: str = ""):
        try:
            object_summary_iterator = self.bucket_interface.objects.all()
            object_keys = [
                obj.key
                for obj in object_summary_iterator
                if obj.key.startswith(f"{self.root_dir}{dir}")
                and obj.key != f"{self.root_dir}{dir}"
            ]
            return object_keys
        except Exception as e:
            raise BucketProxyException(f"Error listing files from bucket, {str(e)}")

    def save_bytes(self, body: bytes, filename: str):
        try:
            self.bucket_interface.put_object(
                Key=f"{self.root_dir}{filename}",
                Body=body,
            )
        except Exception as e:
            raise BucketProxyException(f"Error saving bytes to bucket, {str(e)}")

    @abstractmethod
    def _configure_s3_object(self, *args, **kwargs):
        pass


class MockBucketProxy(BucketProxyBase):
    def __init__(self, bucket_name, root_dir, mock_config={}) -> None:
        super().__init__(bucket_name, root_dir)
        self.bucket_interface = MagicMock()

    def _configure_s3_object(self, object_key):
        class ObjectMock:
            def read(self):
                return json.dumps({"test": "ok", "object_key": object_key})

            def get(self):
                response = {"Body": self}
                return response

        return ObjectMock()


class BucketProxy(BucketProxyBase):
    def __init__(self, bucket_name, root_dir) -> None:
        super().__init__(bucket_name, root_dir)
        self.bucket_interface = boto3.resource("s3").Bucket(bucket_name)

    def _configure_s3_object(self, object_key):
        return boto3.resource("s3").Object(
            self.bucket_name, f"{self.root_dir}{object_key}"
        )
