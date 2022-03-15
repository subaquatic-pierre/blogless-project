output "api_execution_arn" {
  description = "Execute ARN for AWS API gateway."

  value = aws_api_gateway_rest_api.main.execution_arn
}
