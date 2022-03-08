from unittest import TestCase
import os
import json
from unittest.mock import MagicMock

from post_manager import PostManager
from bucket_proxy import BaseBucketProxy


class BucketTestProxy(BaseBucketProxy):
    def get_json(self, filename):
        cwd = os.path.basename(os.path.dirname(__file__))
        file = open(f"{cwd}/fixtures/blog/{filename}")
        content = json.loads(file.read())
        file.close()
        return content

    def save_json(self):
        pass


class TestPostManager(TestCase):
    def setUp(self) -> None:
        super().setUp()
        bucket_proxy = BucketTestProxy("serverless-blog-contents", "blog/")
        self.blog_manager = PostManager("Blog", bucket_proxy)

    def test_list_all(self):
        all_posts = self.blog_manager.list_all()
        self.assertNotEqual(all_posts, 0, "No posts returned from index call")

    def test_title_to_id_success(self):
        post_id = self.blog_manager.title_to_id("Nervous Poincare")
        self.assertIsInstance(post_id, int)

    def test_title_to_id_not_found(self):
        with self.assertRaises(Exception) as context:
            self.blog_manager.title_to_id("Nervous")

        self.assertTrue("No blog with that title found" in str(context.exception))
