data "archive_file" "lambda_functions" {
  type = "zip"

  source_dir  = "${path.module}/postmanager"
  output_path = "${path.module}/functions.zip"
}

resource "aws_lambda_function" "list" {
  function_name    = "List"
  s3_bucket        = aws_s3_bucket.lambda_bucket.id
  s3_key           = aws_s3_object.lambda_functions.key
  runtime          = "python3.9"
  handler          = "http_methods.list"
  source_code_hash = data.archive_file.lambda_functions.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
}

resource "aws_lambda_function" "get" {
  function_name    = "Get"
  s3_bucket        = aws_s3_bucket.lambda_bucket.id
  s3_key           = aws_s3_object.lambda_functions.key
  runtime          = "python3.9"
  handler          = "http_methods.get"
  source_code_hash = data.archive_file.lambda_functions.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
}

resource "aws_lambda_function" "put" {
  function_name    = "Put"
  s3_bucket        = aws_s3_bucket.lambda_bucket.id
  s3_key           = aws_s3_object.lambda_functions.key
  runtime          = "python3.9"
  handler          = "http_methods.put"
  source_code_hash = data.archive_file.lambda_functions.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
}

resource "aws_lambda_function" "post" {
  function_name    = "Post"
  s3_bucket        = aws_s3_bucket.lambda_bucket.id
  s3_key           = aws_s3_object.lambda_functions.key
  runtime          = "python3.9"
  handler          = "http_methods.post"
  source_code_hash = data.archive_file.lambda_functions.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
}

resource "aws_lambda_function" "delete" {
  function_name    = "Delete"
  s3_bucket        = aws_s3_bucket.lambda_bucket.id
  s3_key           = aws_s3_object.lambda_functions.key
  runtime          = "python3.9"
  handler          = "http_methods.delete"
  source_code_hash = data.archive_file.lambda_functions.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
}







