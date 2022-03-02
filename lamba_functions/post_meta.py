from turtle import title
from abc import ABC
import boto3
import json

import boto3

s3 = boto3.resource("s3")


class PostMetaData:
    def __init__(self, post_id, title, dir_key, time_stamp) -> None:
        self.id = post_id
        self.title = title
        self.dir_key = dir_key
        self.time_stamp = time_stamp
