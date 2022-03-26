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
