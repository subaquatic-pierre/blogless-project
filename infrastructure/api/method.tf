resource "aws_api_gateway_method" "list_blog" {
  rest_api_id   = aws_api_gateway_rest_api.main.id
  resource_id   = aws_api_gateway_resource.list_blog.id
  http_method   = "GET"
  authorization = "NONE"
}
