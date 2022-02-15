import json
from names_generator import generate_name
import boto3

s3 = boto3.client("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog/"
index_response = s3.get_object(Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}index.json")

# Get initial data
index = json.loads(index_response["Body"].read())
blog_id = 1
blog_data = next((blog for blog in index if blog["id"] == blog_id), None)

try:
    blog_dir_contents = s3.list_objects_v2(Bucket=BUCKET, Prefix=blog_data["dir_key"])
    for object in blog_dir_contents["Contents"]:
        res = s3.delete_object(Bucket=BUCKET, Key=object["Key"])

    # update index
    updated_index = [blog for blog in index if blog["id"] != blog_id]
    print(updated_index)

    index_res = s3.put_object(
        Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}index.json", Body=json.dumps(updated_index)
    )
    print(index_res)

except Exception:
    raise Exception("Blog with that ID not found")
