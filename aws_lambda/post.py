import json
from postmanager.manager import PostManager
from postmanager.response import Response


def post(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    post_manager, _ = PostManager.setup(
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

        # Get data from body
        meta_data = req_body.get("metaData")
        title = meta_data.get("title")
        content = req_body.get("content")

        # create post
        post = post_manager.create_post(title, content)

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
