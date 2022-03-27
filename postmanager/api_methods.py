import json
from post import Post
from meta import PostMeta
from proxy import BucketProxy
from manager import PostManager
from response import Response

BUCKET_NAME = "serverless-blog-contents"


def list(event, context):
    params = event.get("queryStringParameters")
    body = {}
    response = Response()

    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    bucket_proxy = BucketProxy(bucket_name=BUCKET_NAME, root_dir=f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    if params:
        title = params.get("title")
        if title:
            post_id = post_manager.title_to_id("Most Amazing")
            body = {"id": post_id}
    else:
        body = post_manager.index

    response.body = body
    return response.format()


def get(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    bucket_proxy = BucketProxy(bucket_name=BUCKET_NAME, root_dir=f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    post_id = int(path.split("/")[-1])

    try:
        post = post_manager.get_by_id(post_id)
    except Exception:
        response = Response({"error": {"message": "Blog not found"}})
        return response.format()

    body = post.to_json()
    response = Response(body)

    return response.format()


def delete(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()
    bucket_proxy = BucketProxy(bucket_name=BUCKET_NAME, root_dir=f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    # get post id
    post_id = int(path.split("/")[-1])

    # delete post
    # post_manager.delete_post(post_id)

    response = Response(post_manager.index)

    return response.format()


def post(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    bucket_proxy = BucketProxy(bucket_name=BUCKET_NAME, root_dir=f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    response = Response()

    try:
        req_body = json.loads(event.get("body"))
    except Exception as e:
        error_message = (
            f'There was an error parsing body. Message: {getattr(e, "message", str(e))}'
        )
        response.error_message = error_message
        return response.format()

    try:
        req_body = json.loads(event.get("body"))

        # Get data from body
        meta_data = req_body.get("metaData")
        title = meta_data.get("title")
        content = req_body.get("content")

        # create post
        post_meta: PostMeta = post_manager.create_meta(title)
        post: Post = post_manager.create_post(post_meta, content)

        # save post
        post_manager.save_post(post)

    except Exception as e:
        error_message = f'There was an error parsing metaData or content. Message: {getattr(e, "message", str(e))}'
        response.error_message = error_message
        return response.format()

    body = {
        "post": post.to_json(),
    }

    response = Response(body)

    return response.format()


def put(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    bucket_proxy = BucketProxy(bucket_name=BUCKET_NAME, root_dir=f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    blog_id = path.split("/")[-1]
    post = post_manager.get_by_id(int(blog_id))

    response = Response(event)
    return response.format()

    # get values from form

    # update post
    response = Response(post.to_json())

    # save post
    # post_manager.save_post(post)

    return response.format()
