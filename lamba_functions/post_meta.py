import boto3

s3 = boto3.resource("s3")


class PostMetaData:
    def __init__(self, post_id, title, time_stamp, template="blog") -> None:
        self.id = post_id
        self.title = title
        self.timestamp = time_stamp
        self.template = template

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": self.timestamp,
            "template": self.template,
        }
