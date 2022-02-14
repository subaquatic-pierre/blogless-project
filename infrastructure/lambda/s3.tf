resource "aws_s3_bucket" "lambda_bucket" {
  bucket        = "serverless-blog-functions"
  force_destroy = true
}

resource "aws_s3_bucket_acl" "lambda_bucket" {
  bucket = aws_s3_bucket.lambda_bucket.id
  acl    = "private"
}


resource "aws_s3_bucket" "blog_contents" {
  bucket        = "serverless-blog-contents"
  force_destroy = true
}

data "archive_file" "lambda_functions" {
  type = "zip"

  source_dir  = "${path.module}/functions"
  output_path = "${path.module}/functions.zip"
}

resource "aws_s3_object" "lambda_functions" {
  bucket = aws_s3_bucket.lambda_bucket.id

  key    = "functions.zip"
  source = data.archive_file.lambda_functions.output_path

  etag = filemd5(data.archive_file.lambda_functions.output_path)
}

