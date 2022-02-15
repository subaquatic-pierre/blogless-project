import json
import time
from names_generator import generate_name
import boto3

s3 = boto3.client("s3")
BUCKET = "serverless-blog-contents"
BLOG_BASE_KEY = "blog"


index_response = s3.get_object(Bucket=BUCKET, Key=f"{BLOG_BASE_KEY}index.json")

# Get initial data
index = json.loads(index_response["Body"].read())
blog_id = 1
blog_data = next((blog for blog in index if blog["id"] == blog_id), None)

try:
    blog_meta_res = s3.get_object(
        Bucket=BUCKET, Key=f"{blog_data['dir_key']}/meta.json"
    )
    blog_meta = json.loads(blog_meta_res["Body"].read())

    blog_content_res = s3.get_object(
        Bucket=BUCKET, Key=f"{blog_data['dir_key']}/content.json"
    )
    blog_content = json.loads(blog_content_res["Body"].read())

    new_blog_title = generate_name(style="capital")
    new_dir_key = (
        f'{BLOG_BASE_KEY}/{blog_id}-{new_blog_title.lower().replace(" ", "-")}'
    )

    # Update blog meta
    new_meta = {
        "id": blog_meta["id"],
        "time_stamp": blog_meta["time_stamp"],
        "title": new_blog_title,
        "dir_key": new_dir_key,
    }

    # update blog contents
    new_content = blog_content.copy()
    print(new_dir_key)
    print(blog_meta["dir_key"])

    res = s3.delete_object(Bucket=BUCKET, Key=f'{blog_meta["dir_key"]}/')

    # update index
    updated_index = [blog for blog in index if blog["id"] != blog_id]
    updated_index.append(new_meta)
    print(updated_index)

    # # write new index
    # s3.put_object(Bucket=BUCKET, Key="index.json", Body=json.dumps(updated_index))

    # # # put new data in new blog dir
    # s3.put_object(
    #     Bucket=BUCKET, Key=f"{new_dir_key}/meta.json", Body=json.dumps(new_meta)
    # )
    # s3.put_object(
    #     Bucket=BUCKET, Key=f"{new_dir_key}/content.json", Body=json.dumps(new_content)
    # )
    # s3.put_object(Bucket=BUCKET, Key=f"{new_dir_key}/images/")

    print("New Blog Meta:")
    print(new_meta)
    print("Content:")
    print(new_content)

except Exception:
    raise Exception("Blog with that ID not found")
