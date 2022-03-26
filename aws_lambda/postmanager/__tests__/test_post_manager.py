from unittest import TestCase
import os
import json
from unittest.mock import MagicMock, call

from postmanager.manager import PostManager
from postmanager.post import Post
from postmanager.meta import PostMetaData
from postmanager.proxy import BucketProxy


BUCKET_NAME = "serverless-blog-contents"
BUCKET_ROOT_DIR = "blog/"


def create_post(error=False):
    # Create post
    post_id = 0
    post_title = "Sometitle"
    timestamp = 000
    post_template = "Blog"
    content = "My amazing content"
    post_bucket_proxy = BucketProxy(
        BUCKET_NAME, f"{BUCKET_NAME,BUCKET_ROOT_DIR}{post_id}"
    )
    post_meta = PostMetaData(post_id, post_title, timestamp, post_template)
    post = Post(post_meta, post_bucket_proxy, content)

    # Configure post mocks
    if error:
        post.save = MagicMock(side_effect=Exception)
    else:
        post.save = MagicMock()
    post.to_json = MagicMock()

    return post


class TestPostManager(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.bucket_proxy = MagicMock()
        self.blog_manager = PostManager("Blog", self.bucket_proxy)

    def test_manager_init_success(self):
        bucket_proxy = MagicMock()
        blog_manager = PostManager("Blog", bucket_proxy)

        blog_manager.bucket_proxy.get_json.assert_called_with("index.json")

    def test_manager_init_setup(self):
        bucket_proxy = MagicMock()
        bucket_proxy.get_json.side_effect = Exception("Boom!")
        blog_manager = PostManager("Blog", bucket_proxy)

        blog_manager.bucket_proxy.save_json.assert_called_with([], "index.json")

    def test_get_index(self):
        attrs = {"get_json.return_value": []}
        self.bucket_proxy.configure_mock(**attrs)
        index = self.blog_manager.index
        self.blog_manager.bucket_proxy.get_json.assert_called_with("index.json")
        self.assertIsInstance(index, list)

    def test_list_all_files(self):
        attrs = {"list_dir.return_value": []}
        self.bucket_proxy.configure_mock(**attrs)
        all_posts = self.blog_manager.list_all_files()

        self.assertTrue(self.blog_manager.bucket_proxy.list_dir.called)
        self.assertIsInstance(all_posts, list)

    def test_get_latest_id(self):
        attrs = {"get_json.return_value": ["first", "second"]}
        self.bucket_proxy.configure_mock(**attrs)
        latest_id = self.blog_manager.get_latest_id()

        self.bucket_proxy.get_json.assert_called_with("index.json")
        self.assertEqual(latest_id, 2)

    def test_get_json(self):
        filename = "filename.txt"
        attrs = {"get_json.return_value": {}}
        self.bucket_proxy.configure_mock(**attrs)
        json_res = self.blog_manager.get_json(filename)

        self.assertIsInstance(json_res, dict)
        self.bucket_proxy.get_json.assert_called_with(filename)

    def test_get_by_id(self):
        post_id = 0
        attrs = {
            "get_json.return_value": [
                {"id": post_id, "title": "Sometitle", "timestamp": 000}
            ]
        }
        self.bucket_proxy.configure_mock(**attrs)

        post = self.blog_manager.get_by_id(post_id)

        self.blog_manager.bucket_proxy.get_json.assert_called_with("index.json")
        self.assertIsInstance(post, Post)
        self.assertEqual(post.id, post_id)

    def test_get_by_id_error(self):
        post_id = 0
        attrs = {
            "get_json.return_value": [
                {"id": "noid", "title": "Sometitle", "timestamp": 000}
            ]
        }
        self.bucket_proxy.configure_mock(**attrs)
        with self.assertRaises(Exception) as e:
            self.blog_manager.get_by_id(post_id)

        self.assertEqual(str(e.exception), "No blog with that ID found")

    def test_title_to_id(self):
        post_id = 0
        post_title = "Sometitle"
        attrs = {
            "get_json.return_value": [
                {"id": post_id, "title": post_title, "timestamp": 000}
            ]
        }
        self.bucket_proxy.configure_mock(**attrs)

        post_id = self.blog_manager.title_to_id(post_title)

        self.blog_manager.bucket_proxy.get_json.assert_called_with("index.json")
        self.assertIsInstance(post_id, int)

    def test_title_to_id_error(self):
        post_id = 0
        attrs = {
            "get_json.return_value": [
                {"id": "noid", "title": "Sometitle", "timestamp": 000}
            ]
        }
        self.bucket_proxy.configure_mock(**attrs)
        with self.assertRaises(Exception) as e:
            self.blog_manager.title_to_id(post_id)

        self.assertEqual(str(e.exception), "No blog with that title found")

    def test_save_post(self):
        post = create_post()

        self.blog_manager._update_index = MagicMock()

        return_value = self.blog_manager.save_post(post)

        self.blog_manager._update_index.assert_called()
        post.save.assert_called_once()
        self.assertEqual(post, return_value)

    def test_save_post_error(self):
        post = create_post(error=True)

        self.blog_manager._update_index = MagicMock()

        with self.assertRaises(Exception) as e:
            self.blog_manager.save_post(post)

        self.blog_manager._update_index.assert_not_called()
        self.assertEqual(str(e.exception), "Post could not be saved")

    # def test_save_post(self):
    #     # Post args
    #     post_id = 0
    #     post_title = "Sometitle"
    #     timestamp = 000
    #     post_template = "Blog"
    #     content = "My amazing content"

    #     bucket_proxy_return_mock_value = []
    #     attrs = {"get_json.return_value": bucket_proxy_return_mock_value}
    #     self.bucket_proxy.configure_mock(**attrs)

    #     # Create post
    #     post_bucket_proxy = BucketProxy(
    #         BUCKET_NAME, f"{BUCKET_NAME,BUCKET_ROOT_DIR}{post_id}"
    #     )
    #     post_meta = PostMetaData(post_id, post_title, timestamp, post_template)
    #     post_meta.to_json = MagicMock()
    #     post = Post(post_meta, post_bucket_proxy, content)

    #     self.blog_manager._update_index = MagicMock()

    #     return_value = self.blog_manager.save_post(post)

    #     self.blog_manager.bucket_proxy.get_json.assert_has_calls(
    #         [call("index.json"), call("index.json")]
    #     )

    #     post.save.assert_called_once()
    #     self.assertEqual(post, return_value)

    # def test_title_to_id_success(self):
    #     post_id = self.blog_manager.title_to_id("Nervous Poincare")
    #     self.assertIsInstance(post_id, int)

    # def test_title_to_id_not_found(self):
    #     with self.assertRaises(Exception) as context:
    #         self.blog_manager.title_to_id("Nervous")

    #     self.assertTrue("No blog with that title found" in str(context.exception))
