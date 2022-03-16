output "api_execution_arn" {
  description = "Execute ARN for AWS API gateway."

  value = aws_api_gateway_rest_api.main.execution_arn
}

output "curl_domain_url" {
  depends_on = [aws_api_gateway_base_path_mapping.main]

  description = "API Gateway Domain URL (self-signed certificate)"
  value       = "curl -H 'Host: ${var.rest_api_domain_name}' https://${aws_api_gateway_domain_name.main.regional_domain_name}${var.rest_api_path} # may take a minute to become available on initial deploy"
}

output "curl_stage_invoke_url" {
  description = "API Gateway Stage Invoke URL"
  value       = "curl ${aws_api_gateway_stage.main.invoke_url}${var.rest_api_path}"
}

output "aws_api_gateway_base_path_mapping" {
  value = aws_api_gateway_base_path_mapping.main
}
