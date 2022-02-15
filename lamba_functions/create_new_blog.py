import json
import time
from names_generator import generate_name
import boto3

s3 = boto3.client("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog"

index_response = s3.get_object(Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}/index.json")

# Get current index
index: list = json.loads(index_response["Body"].read())


# Define new blog data
new_blog_id = index.length
blog_name = generate_name(style="capital")

new_dir_key = f'{BLOG_BASE_KEY}/{new_blog_id}-{blog_name.lower().replace(" ", "-")}/'
time_stamp = int(time.time())

contents = json.loads("./blog_template/contents.json")
meta_data = {
    "id": new_blog_id,
    "time_stamp": time_stamp,
    "title": blog_name,
    "dir_key": new_dir_key,
}

# Create blog dir
s3.put_object(Bucket=BUCKET, Key=new_dir_key)

# upload meta data
s3.put_object(Bucket=BUCKET, Key=f'{new_dir_key}/meta.json',Body=json.dumps(meta_data))

# upload contents
s3.put_object(Bucket=BUCKET, Key=)

# upload images
s3.put_object(Bucket=BUCKET, Key=)



index.push(meta_data)

print(index)
print(contents)
