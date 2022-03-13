output "bucket_main" {
  value = aws_s3_bucket.frontend_main
}

output "cf_distribution_id_main" {
  value = aws_cloudfront_distribution.frontend_main.id
}
