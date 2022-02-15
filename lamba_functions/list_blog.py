import json
import boto3

s3 = boto3.client("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog"

index_response = s3.get_object(Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}/index.json")

index = json.loads(index_response["Body"].read())

for blog in index:
    print(blog)
