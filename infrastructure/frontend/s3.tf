# S3 bucket for main website
# --------------------

resource "aws_s3_bucket" "main" {
  bucket        = var.domain_name
  force_destroy = true
}

resource "aws_s3_bucket_website_configuration" "main" {
  bucket = aws_s3_bucket.main.bucket

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "/index.html"
  }

}


# S3 bucket for redirection
# --------------------

resource "aws_s3_bucket" "redirect" {
  bucket        = "www.${var.domain_name}"
  force_destroy = true
}

resource "aws_s3_bucket_website_configuration" "redirect" {
  bucket = aws_s3_bucket.redirect.bucket

  redirect_all_requests_to {
    host_name = var.domain_name
    protocol  = "https"
  }
}


resource "aws_s3_bucket_policy" "main" {
  bucket = aws_s3_bucket.main.id

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": {
              "AWS": "${aws_cloudfront_origin_access_identity.main.iam_arn}"
              },
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::${var.domain_name}/*"
            ]
        }
    ]
}
POLICY
}
