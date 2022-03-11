from time import time
import os
from names_generator import generate_name
import json


from manager import PostManager
from meta import PostMetaData
from proxy import BucketProxy
from post import Post

bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)


def create_post(title, content, image):
    new_id = post_manager.get_latest_id()
    timestamp = int(time())

    bucket_proxy = BucketProxy(
        post_manager.bucket_proxy.bucket_name,
        f"{post_manager.bucket_proxy.root_dir}{new_id}/",
    )
    meta = PostMetaData(new_id, title, timestamp, post_manager.template_name)

    post = Post(meta, bucket_proxy, content, image)
    post_manager.save_post(post)

    return post


def get_dummy_data():
    cwd = os.getcwd()
    file = open(f"{cwd}/blog_template/0/content.json")
    content = json.loads(file.read())
    file.close()

    image_file = open(f"{cwd}/blog_template/0/images/template.jpg", "rb")
    image = image_file.read()
    image_file.close()

    blog_title = generate_name(style="capital")

    return {"title": blog_title, "content": content, "image": image}
