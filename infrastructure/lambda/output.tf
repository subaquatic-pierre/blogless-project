output "lambda_exec_iam_arn" {
  value = aws_iam_role.lambda_exec.arn
}

# lambda invoke ARN
output "lambda_list_invoke_arn" {
  value = aws_lambda_function.list.invoke_arn
}
output "lambda_get_invoke_arn" {
  value = aws_lambda_function.get.invoke_arn
}
output "lambda_post_invoke_arn" {
  value = aws_lambda_function.post.invoke_arn
}
output "lambda_put_invoke_arn" {
  value = aws_lambda_function.put.invoke_arn
}
output "lambda_delete_invoke_arn" {
  value = aws_lambda_function.delete.invoke_arn
}




