import json
import time
from names_generator import generate_name
import boto3

s3 = boto3.client("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog"

response = s3.get_object(Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}/index.json")

# Get current index
index = json.loads(response["Body"].read())

new_blog_id = index.length
blog_name = generate_name(style="capital")
time_stamp = int(time.time())

new_entry = {"id": new_blog_id, "time_stamp": time_stamp, "title": blog_name}
