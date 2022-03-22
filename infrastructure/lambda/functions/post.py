from time import time
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

    body = event.get("body")

    # get latest post id
    new_id = post_manager.get_latest_id()

    # get form data
    title = "Most Amazing"
    timestamp = int(time())

    content = {"aweseme": "awesome sesame streats"}

    # create post
    # meta = PostMetaData(new_id, title, timestamp, template_str)
    # post = Post(meta, bucket_proxy, content)

    # save post
    # post_manager.save_post(post)

    response = Response(body)

    return response.format()
