from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy
from postmanager.response import Response


def list(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()
    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    response = Response(post_manager.index)

    return response.to_json()


def get(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    print(path)

    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    blog_id = path.split("/")[-1]

    post = post_manager.get_by_id(int(blog_id))

    body = post.to_json()
    response = Response(body)

    return response.to_json()
