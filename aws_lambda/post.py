from time import time
import json
from postmanager.manager import PostManager
from postmanager.response import Response
from postmanager.post import Post
from postmanager.meta import PostMetaData


def post(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    post_manager, bucket_proxy = PostManager.setup(
        "serverless-blog-contents", template_name, f"{template_str}/"
    )

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

        # get latest post id
        new_id = post_manager.get_latest_id()

        # get form data
        meta_data = req_body.get("metaData")
        title = meta_data.get("title")
        timestamp = int(time())

        content = req_body.get("content")

        # create post
        meta = PostMetaData(new_id, title, timestamp, template_str)
        post = Post(meta, bucket_proxy, content)

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
