resource "aws_api_gateway_rest_api" "main" {
  name        = "ServerlessBlog"
  description = "REST API for serverless blog application"
}








# resource "aws_api_gateway_rest_api" "main" {
#   body = jsonencode({
#     openapi = "3.0.1"
#     info = {
#       title   = var.rest_api_name
#       version = "1.0"
#     }
#     paths = {
#       (var.rest_api_path) = {
#         get = {
#           x-amazon-apigateway-integration = {
#             httpMethod           = "GET"
#             payloadFormatVersion = "1.0"
#             type                 = "HTTP_PROXY"
#             uri                  = "https://ip-ranges.amazonaws.com/ip-ranges.json"
#           }
#         }
#       }
#     }
#   })

#   name = var.rest_api_name

#   endpoint_configuration {
#     types = ["REGIONAL"]
#   }
# }

# resource "aws_api_gateway_deployment" "main" {
#   rest_api_id = aws_api_gateway_rest_api.main.id

#   lifecycle {
#     create_before_destroy = true
#   }
# }

# resource "aws_api_gateway_stage" "main" {
#   deployment_id = aws_api_gateway_deployment.main.id
#   rest_api_id   = aws_api_gateway_rest_api.main.id
#   stage_name    = "main"
# }

# resource "aws_api_gateway_method_settings" "main" {
#   rest_api_id = aws_api_gateway_rest_api.main.id
#   stage_name  = aws_api_gateway_stage.main.stage_name
#   method_path = "*/*"

#   settings {
#     metrics_enabled = true
#   }
# }
