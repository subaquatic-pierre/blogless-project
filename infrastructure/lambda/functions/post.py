from time import time
import json
from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy
from postmanager.response import Response
from postmanager.post import Post
from postmanager.meta import PostMetaData


def post(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()
    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    body = event.get("body")

    # get latest post id
    new_id = post_manager.get_latest_id()

    # get form data
    title = "Most Amazing"
    timestamp = int(time())

    content = {"aweseme": "awesome sesame streats"}

    # create post
    meta = PostMetaData(new_id, title, timestamp, template_str)
    post = Post(meta, bucket_proxy, content)

    # save post
    post_manager.save_post(post)

    response = Response(body)

    return response.format()
