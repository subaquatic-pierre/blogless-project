import json
from unittest import TestCase
from .utils import create_event_and_context
from api_methods import get, list, post


class TestApiMethods(TestCase):
    def test_get_method(self):
        post_id = 0
        event, context = create_event_and_context(f"/blog/{post_id}", mock_bucket=True)
        blog = get(event, context)
        return blog

    def test_list_method(self):
        event, context = create_event_and_context(f"/blog", mock_bucket=True)
        return list(event, context)

    def test_post_method(self):
        post_body = {
            "metaData": {"title": "Gyming Life"},
            "content": {"Heading": "To be the best you have to be the best"},
        }
        event, context = create_event_and_context(
            "/blog", json.dumps(post_body), mock_bucket=True
        )
        response = post(event, context)
        return response