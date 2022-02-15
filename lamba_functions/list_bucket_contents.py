import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("serverless-blog-contents")
object_summary_iterator = bucket.objects.all()

for object_summary in object_summary_iterator:
    object = s3.Object(object_summary.bucket_name, object_summary.key)
    object.download_file("./blog")
    print(object)
