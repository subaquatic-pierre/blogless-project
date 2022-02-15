import json
import time
from names_generator import generate_name
import boto3

s3 = boto3.client("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog/"

index_response = s3.get_object(Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}index.json")

index = json.loads(index_response["Body"].read())

blog_id = 1

blog_data = next((blog for blog in index if blog["id"] == blog_id), None)

try:
    blog_meta_res = s3.get_object(Bucket=BUCKET, Key=f"{blog_data['dir_key']}meta.json")
    blog_meta = json.loads(blog_meta_res["Body"].read())

    blog_content_res = s3.get_object(
        Bucket=BUCKET, Key=f"{blog_data['dir_key']}content.json"
    )
    blog_content = json.loads(blog_content_res["Body"].read())

    print("Blog Meta:")
    print(blog_meta)
    print("Content:")
    print(blog_content)

except Exception:
    raise Exception("Blog with that ID not found")
