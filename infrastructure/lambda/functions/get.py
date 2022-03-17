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

    return response.format()


def get(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    post_id = int(path.split("/")[-1])

    post = post_manager.get_by_id(post_id)

    body = post.to_json()
    response = Response(body)

    return response.format()


def title_to_id(event, context):
    # path = event.get("path")
    # query_string = event.get("querystring")

    response = Response(event)

    return response.format()

    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    print(path)

    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

    post_id = post_manager.title_to_id()
