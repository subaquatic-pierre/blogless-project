from enum import Enum, auto
import json
from response import Response


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
        self.body = self._parse_body(event)
        self.query_string_params = self._parse_query_string_params(event)

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

    def return_response(self):
        return self.reponse.format()

    def get_query_string_params(self):
        return self.query_string_params

    # Private response setters
    def _set_response_error(self, message, e=""):
        text = f'{message}. {getattr(e, "message", str(e))}'
        self.reponse.error_message = text

    def _set_response_body(self, body):
        self.reponse.body = body

    # Private method handlers
    def _handle_get_method(self):
        pass

    def _handle_list_method(self):
        if self.query_string_params:
            title = self.query_string_params.get("title")
            if title:
                post_id = self.post_manager.title_to_id("Most Amazing")
                body = {"id": post_id}
        else:
            body = self.post_manager.index

        self._set_response_body(body)

    def _handle_put_method(self):
        pass

    def _handle_post_method(self):
        pass

    def _handle_delete_method(self):
        pass

    def _parse_body(self, event):
        try:
            body = json.loads(event.get("body"))
            return body
        except Exception as e:
            self._set_response_error("There was an error parsing event body.", e)

    def _parse_query_string_params(self, event):
        params = event.get("queryStringParameters")
        return params
