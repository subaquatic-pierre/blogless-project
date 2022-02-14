resource "random_pet" "lambda_bucket_name" {
  prefix = "serverless-blog-functions"
  length = 4
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = random_pet.lambda_bucket_name.id

  #   acl           = "private"
  force_destroy = true
}

data "archive_file" "lambda_hello" {
  type = "zip"

  source_dir  = "${path.root}/functions/hello"
  output_path = "${path.root}/functions/hello.zip"
}

resource "aws_s3_object" "lambda_hello" {
  bucket = aws_s3_bucket.lambda_bucket.id

  key    = "hello.zip"
  source = data.archive_file.lambda_hello.output_path

  etag = filemd5(data.archive_file.lambda_hello.output_path)
}

