from enum import Enum, auto
import json
from response import Response
from meta import PostMeta
from post import Post


class MethodType(Enum):
    GET = auto()
    LIST = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()


class MethodHandler:
    def __init__(self, post_manager, event) -> None:
        self.post_manager = post_manager
        self.reponse = Response()

        # parse attrs from event
        self.request_body = self._parse_body(event)
        self.query_string_params = self._parse_query_string_params(event)
        self.path = self._parse_path(event)

    def return_response(self):
        return self.reponse.format()

    def handle_method(self, method_type: MethodType):
        if method_type == MethodType.GET:
            self._handle_get_method()
        elif method_type == MethodType.LIST:
            self._handle_list_method()
        elif method_type == MethodType.POST:
            self._handle_post_method()
        elif method_type == MethodType.PUT:
            self._handle_put_method()
        elif method_type == MethodType.DELETE:
            self._handle_delete_method()

    # --- METHOD HANDLERS ---
    def _handle_get_method(self):
        post_id = self.path.split("/")[-1]

        try:
            post = self.post_manager.get_by_id(post_id)
        except Exception as e:
            self._set_response_error("Blog not found", e)
            return

        body = {
            "post": post.to_json(),
        }
        self._set_response_body(body)

    def _handle_list_method(self):
        try:
            if self.query_string_params:
                title = self.query_string_params.get("title")
                if title:
                    post_id = self.post_manager.title_to_id("Most Amazing")
                    body = {"id": post_id}
            else:
                body = self.post_manager.index
        except Exception as e:
            self._set_response_error("Unable to list posts", e)
            return

        self._set_response_body(body)

    def _handle_post_method(self):
        try:
            meta_data = self.request_body.get("metaData")
        except Exception as e:
            self._set_response_error(
                "There was an error getting metaData from request body", e
            )
            return

        try:
            content = self.request_body.get("content")
        except Exception as e:
            self._set_response_error(
                "There was an error getting content from request body", e
            )
            return

        title = meta_data.get("title")

        try:
            post_meta: PostMeta = self.post_manager.create_meta(title)
            post: Post = self.post_manager.create_post(post_meta, content)

        except Exception as e:
            self._set_response_error("There was an error creating post", e)
            return

        try:
            self.post_manager.save_post(post)
        except Exception as e:
            self._set_response_error("There was an error saving post", e)
            return

        body = {
            "post": post.to_json(),
        }
        self._set_response_body(body)

    def _handle_put_method(self):
        pass

    def _handle_delete_method(self):
        pass

    # --- END METHOD HANDLERS ---

    def _set_response_error(self, message, e=""):
        text = f'{message}. {getattr(e, "message", str(e))}'
        self.reponse.error_message = text

    def _set_response_body(self, body):
        self.reponse.body = body

    def _parse_body(self, event):
        try:
            body = json.loads(event.get("body"))
            return body
        except Exception as e:
            self._set_response_error("There was an error parsing event body", e)

    def _parse_query_string_params(self, event):
        params = event.get("queryStringParameters")
        return params

    def _parse_path(self, event):
        path = event.get("path")
        return path
