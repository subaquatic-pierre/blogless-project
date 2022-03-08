from abc import ABC
import boto3
import json

import boto3

s3 = boto3.resource("s3")


class PostMetaData:
    def __init__(self, post_id, title, time_stamp) -> None:
        self.id = post_id
        self.title = title
        self.timestamp = time_stamp

    def to_json(self):
        return {"id": self.id, "title": self.title, "timestamp": self.timestamp}
