import json
from unittest import TestCase
from unittest.mock import MagicMock

from proxy import BucketProxy
from .utils import BUCKET_NAME, BUCKET_ROOT_DIR


class KeyMock:
    def __init__(self, key) -> None:
        self.key = key


class BodyMock:
    def read(self):
        return json.dumps({"test": "ok"})


class ObjectMock:
    def __init__(self, bucket_name, object_key) -> None:
        self.bucket_name = bucket_name
        self.key = object_key

    def get():
        response = {"Body": BodyMock()}
        return response


class ResourceMock:
    class Object:
        def __init__(self, bucket_name, object_key) -> None:
            self.bucket_name = bucket_name
            self.key = object_key

        def get(self):
            response = {"Body": BodyMock()}
            return response


class BucketInterfaceMock:
    def put_object(self):
        return MagicMock

    def delete_files(self):
        return MagicMock

    def list_dir(self, dir):
        return MagicMock

    def save_bytes(self, body, filename):
        return MagicMock


class BucketProxyTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bucket = BucketProxy(BUCKET_NAME, BUCKET_ROOT_DIR, test_bucket=True)
        self.bucket.bucket_interface = MagicMock()
        self.bucket.s3_interface = ResourceMock

    def test_get_json(self):
        bucket = BucketProxy(BUCKET_NAME, self.bucket.root_dir, test_bucket=True)
        # bucket.s3_interface.Object = MagicMock(return_value=ObjectMock)
        object_key = "index.json"
        json = bucket.get_json(object_key)

        # bucket.s3_interface.Object.assert_called_once_with(
        #     BUCKET_NAME, f"{self.bucket.root_dir}{object_key}"
        # )
        # self.assertIn("test", json)
        self.assertIsInstance(json, dict)

    def test_get_json_resource_mock(self):
        object_key = "index.json"
        json = self.bucket.get_json(object_key)
        self.assertIsInstance(json, dict)

    def test_save_json(self):
        filename = "filename.txt"
        body = {}
        self.bucket.save_json(body, filename)

        call_count = self.bucket.bucket_interface.put_object.call_count
        self.assertEqual(call_count, 2)

        self.bucket.bucket_interface.put_object.assert_called_with(
            Key=f"{self.bucket.root_dir}{filename}", Body=json.dumps(body)
        )

    def test_delete_files(self):
        filenames = ["filename1.txt", "filename1.txt"]

        self.bucket.delete_files(filenames)
        objects = [{"Key": filename} for filename in filenames]
        self.bucket.bucket_interface.delete_objects.assert_called_with(
            Delete={"Objects": objects}
        )

    def test_delete_files_empty_array(self):
        filenames = []

        self.bucket.delete_files(filenames)
        self.bucket.bucket_interface.delete_objects.assert_not_called()

    def test_list_dir(self):
        key_list = [
            f"{self.bucket.root_dir}something",
            f"{self.bucket.root_dir}somethingelse",
        ]

        all_dirs = [KeyMock(key_list[0]), KeyMock(key_list[1])]

        self.bucket.bucket_interface.objects.all = MagicMock(return_value=all_dirs)
        dir_response = self.bucket.list_dir()
        self.bucket.bucket_interface.objects.all.assert_called_once()

        self.assertIsInstance(dir_response, list)
        self.assertEqual(key_list, dir_response)

    def test_save_bytes(self):
        body = b"0x00"
        filename = "something.jpg"
        self.bucket.save_bytes(body, filename)

        call_count = self.bucket.bucket_interface.put_object.call_count

        self.bucket.bucket_interface.put_object.assert_called_with(
            Key=f"{self.bucket.root_dir}{filename}", Body=body
        )
