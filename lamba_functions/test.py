from post_manager import PostManager
from bucket_proxy import BucketProxy
import json
import os
from names_generator import generate_name

bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)

all_posts = post_manager.list_all()
print(all_posts)

# title = post_manager.title_to_id("Recursing Hypatia")
# print(title)

# post = post_manager.get_by_id(0)
# print(post.content)

# Create test post
# cwd = os.getcwd()
# file = open(f"{cwd}/blog_template/0/content.json")
# content = json.loads(file.read())
# file.close()

# image_file = open(f"{cwd}/blog_template/0/images/template.jpg", "rb")
# image = image_file.read()
# image_file.close()

# blog_title = generate_name(style="capital")
# new_post = post_manager.create_post(blog_title, content, image)

# List all items in post bucket
post = post_manager.get_by_id(0)
# items = post.list_files()
# print(items)
# print(post)
urls = post.list_image_urls()
print(urls)
