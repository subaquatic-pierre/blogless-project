from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy
from postmanager.response import Response


def put(event, context):
    path = event.get("path")
    template_str = path.split("/")[1]
    template_name = template_str.capitalize()

    bucket_proxy = BucketProxy("serverless-blog-contents", f"{template_str}/")
    post_manager = PostManager(template_name, bucket_proxy)

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
