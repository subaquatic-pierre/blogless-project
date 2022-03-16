output "bucket_main" {
  value = aws_s3_bucket.main
}

output "cf_distribution_id_main" {
  value = aws_cloudfront_distribution.main.id
}

output "acm_certificate_domain_name" {
  description = "Domain name for acm certificate"
  value       = aws_acm_certificate.main.domain_name
}

output "acm_certificate_arn" {
  description = "ARN fro ACM certificate"
  value       = aws_acm_certificate.main.arn
}
