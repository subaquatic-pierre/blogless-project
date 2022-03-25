import json
from unittest import TestCase
from unittest.mock import MagicMock

from postmanager.proxy import BucketProxy

BUCKET_NAME = "serverless-blog-contents"
BUCKET_ROOT_DIR = "blog/"


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
    pass


class BucketProxyTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bucket = BucketProxy(BUCKET_NAME, BUCKET_ROOT_DIR)
        self.bucket.bucket_interface = BucketInterfaceMock
        self.bucket.s3_interface = ResourceMock

    def test_get_json(self):
        bucket = BucketProxy(BUCKET_NAME, BUCKET_ROOT_DIR)
        bucket.s3_interface.Object = MagicMock(return_value=ObjectMock)
        obect_key = "index.json"
        json = bucket.get_json(obect_key)
        bucket.s3_interface.Object.assert_called_once_with(
            BUCKET_NAME, f"{BUCKET_ROOT_DIR}{obect_key}"
        )
        self.assertIn("test", json)

    def test_get_json_resource_mock(self):
        object_key = "index.json"
        json = self.bucket.get_json(object_key)
        self.assertIn("test", json)
