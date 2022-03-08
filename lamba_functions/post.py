import os
from bucket_proxy import BucketProxy
from post_meta import PostMetaData


class Post:
    def __init__(
        self, meta_data: PostMetaData, bucket_proxy: BucketProxy, content, image=None
    ) -> None:
        self.id = meta_data.id
        self.bucket_proxy = bucket_proxy
        self.meta_data = meta_data
        self._content = content
        self.image = image

    @property
    def title(self):
        return self.meta_data.title

    @property
    def content(self):
        content = self.bucket_proxy.get_json("content.json")
        return content

    def save(self):
        # Save content
        self.bucket_proxy.save_json(self._content, "content.json")
        # Save meta
        self.bucket_proxy.save_json(self.meta_data.to_json(), "meta.json")

        # Save images, for image in images
        if self.image != None:
            self.bucket_proxy.save_file(self.image, f"images/template.jpg")

    def __str__(self):
        return f"ID: {self.id}, Title: {self.meta_data.title}"
