from manager import PostManager

blog_manager = PostManager("serverless-blog-contents", "blog/", "Blog")
print(blog_manager.index)
