# resource "aws_lambda_permission" "list_all" {
#   statement_id  = "AllowExecutionFromAPIGateway"
#   action        = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.list_all.function_name
#   principal     = "apigateway.amazonaws.com"
#   source_arn    = "${var.api_execution_arn}/*/*/*"
# }
