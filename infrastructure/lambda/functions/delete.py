from postmanager.manager import PostManager
from postmanager.response import Response


def delete(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()
    post_manager, _ = PostManager.setup(
        "serverless-blog-contents", template_name, f"{template_str}/"
    )

    # get post id
    post_id = int(path.split("/")[-1])

    # delete post
    # post_manager.delete_post(post_id)

    response = Response(post_manager.index)

    return response.format()
