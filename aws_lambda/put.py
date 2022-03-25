from postmanager.manager import PostManager
from postmanager.response import Response


def put(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    post_manager, _ = PostManager.setup(
        "serverless-blog-contents", template_name, f"{template_str}/"
    )

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
