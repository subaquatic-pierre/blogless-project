from postmanager.manager import PostManager
from postmanager.response import Response


def list(event, context):
    params = event.get("queryStringParameters")
    body = {}
    response = Response()

    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()
    post_manager, _ = PostManager.setup(
        "serverless-blog-contents", template_name, f"{template_str}/"
    )

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

    post_manager, _ = PostManager.setup(
        "serverless-blog-contents", template_name, f"{template_str}/"
    )
    post_id = int(path.split("/")[-1])

    post = post_manager.get_by_id(post_id)

    body = post.to_json()
    response = Response(body)

    return response.format()
