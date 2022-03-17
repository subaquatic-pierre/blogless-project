resource "aws_lambda_function" "list" {
  function_name = "List"

  s3_bucket = aws_s3_bucket.lambda_bucket.id
  s3_key    = aws_s3_object.lambda_functions.key

  runtime = "python3.9"
  handler = "get.list"

  source_code_hash = data.archive_file.lambda_functions.output_base64sha256

  role = aws_iam_role.lambda_exec.arn
}

resource "aws_lambda_function" "get" {
  function_name = "Get"

  s3_bucket = aws_s3_bucket.lambda_bucket.id
  s3_key    = aws_s3_object.lambda_functions.key

  runtime = "python3.9"
  handler = "get.get"

  source_code_hash = data.archive_file.lambda_functions.output_base64sha256

  role = aws_iam_role.lambda_exec.arn
}





