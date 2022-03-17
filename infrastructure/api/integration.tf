resource "aws_api_gateway_integration" "list_blog" {
  rest_api_id             = aws_api_gateway_rest_api.main.id
  resource_id             = aws_api_gateway_resource.list_blog.id
  http_method             = aws_api_gateway_method.list_blog.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = var.lambda_list_all_invoke_arn
}
