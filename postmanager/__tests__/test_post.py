from unittest import TestCase
from unittest.mock import MagicMock

from manager import PostManager, BucketProxy


class TestPost(TestCase):
    pass
    # def test_save_post(self):
    #     post = self.blog_manager.create_post("Amazing Post", {"data": "Amazing data"})
    #     post.bucket_proxy = create_dummy_bucket_proxy()

    #     self.blog_manager._update_index = MagicMock()

    #     return_value = self.blog_manager.save_post(post)

    #     self.blog_manager._update_index.assert_called()
    #     # post.save.assert_called_once()

    #     print(post.bucket_proxy.save_json.call_args_list)
    #     self.assertEqual(post, return_value)
