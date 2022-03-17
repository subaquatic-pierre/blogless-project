resource "aws_iam_role" "lambda_exec" {
  name = "serverless_lambda"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_bucket_policy" {
  name = "bucket_policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:ListBucket",
        ]
        Sid    = "ListObjectsInBucket",
        Effect = "Allow"
        Resource = [
          "arn:aws:s3:::${aws_s3_bucket.lambda_bucket.id}"
        ]
      },
      {
        Action = [
          "s3:*Object",
        ]
        Sid    = "AllObjectActions",
        Effect = "Allow"
        Resource = [
          "arn:aws:s3:::${aws_s3_bucket.lambda_bucket.id}"
        ]
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.lambda_bucket_policy.arn
}
