from unittest import TestCase
import os
import json
from unittest.mock import MagicMock

from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy


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

    # def test_list_all(self):
    #     all_posts = self.blog_manager.list_all()
    #     self.assertNotEqual(all_posts, 0, "No posts returned from index call")

    # def test_title_to_id_success(self):
    #     post_id = self.blog_manager.title_to_id("Nervous Poincare")
    #     self.assertIsInstance(post_id, int)

    # def test_title_to_id_not_found(self):
    #     with self.assertRaises(Exception) as context:
    #         self.blog_manager.title_to_id("Nervous")

    #     self.assertTrue("No blog with that title found" in str(context.exception))

    def test_create_post(self):
        index = [
            {"id": 0, "time_stamp": 1646289628, "title": "Nervous Poincare"},
            {"id": 1, "time_stamp": 1646289718, "title": "Recursing Hypatia"},
        ]
        content = {
            "time": 1550476186479,
            "blocks": [
                {
                    "type": "paragraph",
                    "data": {
                        "text": "The example of text that was written in <b>one of popular</b> text editors."
                    },
                },
                {
                    "type": "header",
                    "data": {"text": "With the header of course", "level": 2},
                },
                {"type": "paragraph", "data": {"text": "So what do we have?"}},
            ],
            "version": "2.8.1",
        }
