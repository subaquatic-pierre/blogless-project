import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("serverless-blog-contents")
object_summary_iterator = bucket.objects.all()

for object in object_summary_iterator:
    print(object)
