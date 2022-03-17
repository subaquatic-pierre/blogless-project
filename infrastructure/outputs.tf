# Output value definitions
output "api_domain_name" {
  description = "Name of the Lambda function."

  value = "api.${var.domain_name}"
}

