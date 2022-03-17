from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy
from postmanager.response import Response


def delete(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()
    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    # get post id
    post_id = int(path.split("/")[-1])

    # delete post
    # post_manager.delete_post(post_id)

    response = Response(post_manager.index)

    return response.format()
