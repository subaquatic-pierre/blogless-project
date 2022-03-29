import json
from post import Post
from meta import PostMeta
from manager import PostManager
from event import Event
from response import Response
from method import (
    DeleteMethod,
    MethodType,
    MethodHandler,
    GetMethod,
    ListMethod,
    PostMethod,
    PutMethod,
)


def format_error_message(message, e):
    return f'{message}. {getattr(e, "message", str(e))}'


def list(event, context):
    request_event = Event(event)

    if request_event.error_message:
        response = Response(error_message=request_event.error_message)
        return response.format()

    post_manager = PostManager.setup_api_post_manager(request_event)

    method = ListMethod(request_event, post_manager)

    method.run()

    response = Response(method.response_body, method.error_message)

    return response.format()


def get(event, context):
    request_event = Event(event)

    if request_event.error_message:
        response = Response(error_message=request_event.error_message)
        return response.format()

    post_manager = PostManager.setup_api_post_manager(request_event)

    method = GetMethod(request_event, post_manager)

    method.run()

    response = Response(method.response_body, method.error_message)

    return response.format()


def post(event, context):
    request_event = Event(event)

    if request_event.error_message:
        response = Response(error_message=request_event.error_message)
        return response.format()

    post_manager = PostManager.setup_api_post_manager(request_event)

    method = PostMethod(request_event, post_manager)

    method.run()

    response = Response(method.response_body, method.error_message)

    return response.format()


def delete(event, context):
    request_event = Event(event)

    if request_event.error_message:
        response = Response(error_message=request_event.error_message)
        return response.format()

    post_manager = PostManager.setup_api_post_manager(request_event)

    method = DeleteMethod(request_event, post_manager)

    method.run()

    response = Response(method.response_body, method.error_message)

    return response.format()


def put(event, context):
    request_event = Event(event)

    if request_event.error_message:
        response = Response(error_message=request_event.error_message)
        return response.format()

    post_manager = PostManager.setup_api_post_manager(request_event)

    method = PutMethod(request_event, post_manager)

    method.run()

    response = Response(method.response_body, method.error_message)

    return response.format()
