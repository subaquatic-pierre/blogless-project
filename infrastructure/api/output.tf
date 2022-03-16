output "api_execution_arn" {
  description = "Execute ARN for AWS API gateway."

  value = aws_api_gateway_rest_api.main.execution_arn
}

output "api_list_blog" {
  value = aws_api_gateway_resource.list_blog.path
}
