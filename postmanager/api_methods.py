import json
from post import Post
from meta import PostMeta
from manager import PostManager
from response import Response
from method import MethodType, MethodHandler


def format_error_message(message, e):
    return f'{message}. {getattr(e, "message", str(e))}'


def list(event, context):
    post_manager = PostManager.setup_api_post_manager(event)
    method_handler = MethodHandler(post_manager, event)

    method_handler.handle_method(MethodType.LIST)

    return method_handler.return_response()


def get(event, context):
    post_manager = PostManager.setup_api_post_manager(event)
    method_handler = MethodHandler(post_manager, event)

    method_handler.handle_method(MethodType.GET)

    return method_handler.return_response()


def post(event, context):
    post_manager = PostManager.setup_api_post_manager(event)
    method_handler = MethodHandler(post_manager, event)

    method_handler.handle_method(MethodType.POST)

    return method_handler.return_response()


def delete(event, context):
    path = event.get("path")
    testing = event.get("test_api", False)
    mock_config = event.get("mock_config", {})

    post_manager = PostManager.setup_post_manager(event)

    # get post id
    post_id = path.split("/")[-1]

    # delete post
    # post_manager.delete_post(post_id)

    response = Response(post_manager.index)

    return response.format()


def put():
    pass


# def put(event, context):
#     path = event.get("path")
#     testing = event.get("test_api", False)
#     mock_config = event.get("mock_config", {})
#     post_id = path.split("/")[-1]

#     post_manager = PostManager.setup_post_manager(event)
#     response = Response()

#     try:
#         body = parse_body(event)
#     except Exception as e:
#         error_message = format_error_message("There was an error parsing body", e)
#         response.error_message = error_message

#     try:
#         meta_data = body.get("metaData")
#         content = body.get("content")

#         # get post
#         post: Post = post_manager.get_by_id(post_id)
#         post_meta = post_manager.get_meta(post_id)

#         post.meta_data = post_meta
#         post.content = content

#     except Exception as e:
#         error_message = format_error_message("There was an error updating post data", e)
#         response.error_message = error_message
#         return response.format()

#     try:
#         post_manager.save_post(post)

#     except Exception as e:
#         error_message = format_error_message("There was an error saving post", e)
#         response.error_message = error_message

#     if response.error_message:
#         return response.format()

#     else:
#         response.body = {"post": post.to_json()}
#         return response.format()
