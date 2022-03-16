# Output value definitions

output "lambda_bucket_name" {
  description = "Name of the S3 bucket used to store function code."

  value = module.lambda.lambda_bucket_name
}

output "function_name" {
  description = "Name of the Lambda function."

  value = module.lambda.function_name
}

# output "api_curl_domain_url" {
#   depends_on = [module.api.aws_api_gateway_base_path_mapping]

#   description = "API Gateway Domain URL (self-signed certificate)"
#   value       = module.api.curl_domain_url
# }

# output "api_curl_stage_invoke_url" {
#   description = "API Gateway Stage Invoke URL"
#   value       = module.api.curl_stage_invoke_url
# }
