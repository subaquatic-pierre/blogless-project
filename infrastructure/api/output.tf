output "api_execution_arn" {
  description = "Execute ARN for AWS API gateway."

  value = aws_api_gateway_rest_api.main.execution_arn
}

output "aws_api_gateway_rest_api_id" {
  description = "Main REST API ID"

  value = aws_api_gateway_rest_api.main.id
}

output "aws_api_gateway_resource_main_id" {
  description = "Blog API resource ID"

  value = aws_api_gateway_resource.blog.id
}

output "aws_api_gateway_resource_blog_id" {
  description = "Blog API resource ID"

  value = aws_api_gateway_resource.get.id
}

