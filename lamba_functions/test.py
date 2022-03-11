from post_manager import PostManager
from bucket_proxy import BucketProxy
import json
import os
from names_generator import generate_name

from create_post import create_post

bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)


# Create test post

# cwd = os.getcwd()
# file = open(f"{cwd}/blog_template/0/content.json")
# content = json.loads(file.read())
# file.close()

# image_file = open(f"{cwd}/blog_template/0/images/template.jpg", "rb")
# image = image_file.read()
# image_file.close()

# blog_title = generate_name(style="capital")
# new_post = create_post(blog_title, content, image, post_manager)
# print(new_post)

# -------------------------------


# List all items in post bucket

# post = post_manager.get_by_id(0)
# items = post.list_files()
# print(items)
# print(post)
# urls = post.list_image_urls()
# print(urls)
print(post_manager.index)

# -------------------------------

# Delete post
# post_id = post_manager.title_to_id("Competent Heyrovsky")
# post = post_manager.get_by_id(post_id)
# post_manager.delete_post(post_id)
