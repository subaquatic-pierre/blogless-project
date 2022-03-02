from lamba_functions.post_manager import PostManager, BucketProxy
from unittest import TestCase
from unittest.mock import MagicMock

blog_manager = PostManager("serverless-blog-contents", "blog/", "Blog")
print(blog_manager.index)


class TestBucketProxy(TestCase):
    pass


class TestPost(TestCase):
    pass


class TestPostManager(TestCase):
    def setUp(self) -> None:
        return super().setUp()
        bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
        bucket_proxy.get_json_data = MagicMock
        self.blog_manager = PostManager("Blog", bucket_proxy)

    def test_return_index(self):
        pass
