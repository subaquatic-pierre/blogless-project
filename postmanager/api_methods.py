import json
from post import Post
from meta import PostMeta
from proxy import BucketProxy, MockBucketProxy
from manager import PostManager
from response import Response

BUCKET_NAME = "serverless-blog-contents"


def format_error_message(message, e):
    return f'{message}. {getattr(e, "message", str(e))}'


def setup_post_manager(path, testing, mock_config={}):
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    if testing:
        bucket_proxy = MockBucketProxy(
            bucket_name=BUCKET_NAME,
            root_dir=f"{template_str}/",
            mock_config=mock_config,
        )
    else:
        bucket_proxy = BucketProxy(
            bucket_name=BUCKET_NAME,
            root_dir=f"{template_str}/",
        )

    post_manager = PostManager(bucket_proxy, template_name)

    return post_manager, bucket_proxy


def parse_body(event):
    body = json.loads(event.get("body"))
    return body


def list(event, context):
    params = event.get("queryStringParameters")
    path = event.get("path")
    testing = event.get("test_api", False)
    mock_config = event.get("mock_config", {})

    post_manager, _ = setup_post_manager(path, testing, mock_config)

    if params:
        title = params.get("title")
        if title:
            post_id = post_manager.title_to_id("Most Amazing")
            body = {"id": post_id}
    else:
        body = post_manager.index

    response = Response(body)
    return response.format()


def get(event, context):
    path = event.get("path")
    testing = event.get("test_api", False)
    mock_config = event.get("mock_config", {})

    post_manager, _ = setup_post_manager(path, testing, mock_config)

    post_id = path.split("/")[-1]

    try:
        post = post_manager.get_by_id(post_id)
    except Exception:
        response = Response({"error": {"message": "Blog not found"}})
        return response.format()

    body = {
        "post": post.to_json(),
    }

    response = Response(body)

    return response.format()


def delete(event, context):
    path = event.get("path")
    testing = event.get("test_api", False)
    mock_config = event.get("mock_config", {})

    post_manager, _ = setup_post_manager(path, testing, mock_config)

    # get post id
    post_id = path.split("/")[-1]

    # delete post
    # post_manager.delete_post(post_id)

    response = Response(post_manager.index)

    return response.format()


def post(event, context):
    path = event.get("path")
    testing = event.get("test_api", False)
    mock_config = event.get("mock_config", {})
    response = Response()

    post_manager, _ = setup_post_manager(path, testing, mock_config)

    try:
        body = parse_body(event)

        # Get data from body
        meta_data = body.get("metaData")
        title = meta_data.get("title")
        content = body.get("content")

        # create post
        post_meta: PostMeta = post_manager.create_meta(title)
        post: Post = post_manager.create_post(post_meta, content)

        # save post
        post_manager.save_post(post)

    except Exception as e:
        error_message = format_error_message(
            "There was an error parsing metaData or content", e
        )
        response.error_message = error_message

    if response.error_message:
        return response.format()
    else:
        body = {
            "post": post.to_json(),
        }
        response.body = body

        return response.format()


def put(event, context):
    path = event.get("path")
    testing = event.get("test_api", False)
    mock_config = event.get("mock_config", {})
    post_id = path.split("/")[-1]

    post_manager, _ = setup_post_manager(path, testing, mock_config)
    response = Response()

    try:
        body = parse_body(event)
    except Exception as e:
        error_message = format_error_message("There was an error parsing body", e)
        response.error_message = error_message

    try:
        meta_data = body.get("metaData")
        content = body.get("content")

        # get post
        post: Post = post_manager.get_by_id(post_id)
        post_meta = post_manager.get_meta(post_id)

        post.meta_data = post_meta
        post.content = content

    except Exception as e:
        error_message = format_error_message("There was an error updating post data", e)
        response.error_message = error_message
        return response.format()

    try:
        post_manager.save_post(post)

    except Exception as e:
        error_message = format_error_message("There was an error saving post", e)
        response.error_message = error_message

    if response.error_message:
        return response.format()

    else:
        response.body = {"post": post.to_json()}
        return response.format()
