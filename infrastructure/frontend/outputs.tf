output "main_bucket_name" {
  description = "Main name for static hosting bucket"

  value = aws_s3_bucket.main.id
}
output "main_bucket_domain_name" {
  description = "Domain name for redirect bucket"

  value = aws_s3_bucket.main.bucket_domain_name
}

output "redirect_bucket_domain_name" {
  description = "Domain name for main bucket"

  value = aws_s3_bucket.redirect.bucket_domain_name
}

output "main_bucket_website_config_website_endpoint" {
  value = aws_s3_bucket_website_configuration.main.website_endpoint
}

output "redirect_bucket_website_config_website_endpoint" {
  value = aws_s3_bucket_website_configuration.redirect.website_endpoint
}

