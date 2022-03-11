from post_manager import PostManager
from bucket_proxy import BucketProxy
import json
import os

bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)

# all_posts = post_manager.list_all()
# print(all_posts)

# title = post_manager.title_to_id("Recursing Hypatia")
# print(title)

# post = post_manager.get_by_id(0)
# print(post.content)

# Create test post
# cwd = os.getcwd()
# print(cwd)
# file = open(f"{cwd}/blog_template/0/content.json")
# content = json.loads(file.read())
# file.close()

# image_file = open(f"{cwd}/blog_template/0/images/template.jpg", "rb")
# image = image_file.read()
# image_file.close()

# new_post = post_manager.create_post("New Amazing Blog", content, image)

# print(post_manager.index)
# files = post_manager.list_all_files()
# print(files)

# List all items in post bucket
post = post_manager.get_by_id(0)
print(post)
# items = post.image_urls()
# print(items)
