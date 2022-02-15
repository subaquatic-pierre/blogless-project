import json
import boto3

s3_client = boto3.client("s3")
s3 = boto3.resource("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog/"


class Directory:
    def __init__(self, bucket, base_key) -> None:
        self.bucket = bucket
        self.key = base_key
        pass

    def get_bucket_object(self):
        return s3_client.get_object(bucket_name=self.bucket, key="/")


class BlogDirectory(Directory):
    def __init__(self) -> None:
        super().__init__(BUCKET, BLOG_BASE_KEY)

    def list_dir(self):
        # partial_list_res = s3_client.list_objects_v2(Bucket=self.bucket, Key=self.key)
        print(self.key)
        dir_list = []

        # for object in partial_list_res["Contents"]:
        #     object_key = object["Key"]
        #     if len(object_key.split("/")) == 2:
        #         dir_list.append(object["Key"])

        return dir_list

    def list_index(self):
        index_response = s3_client.get_object(
            Bucket=BUCKET, Key=f"{self.key}index.json"
        )

        index = json.loads(index_response["Body"].read())
        return index
