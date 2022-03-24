terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }

  required_version = "~> 1.0"
}

provider "aws" {
  region = "us-east-1"
}

# terraform {
#   backend "s3" {
#     bucket = "terraform-serverless-backend"
#     key    = "tfstate/terraform-backend"
#     region = "us-east-2"
#   }
# }

module "api" {
  source              = "./api"
  domain_name         = var.domain_name
  acm_certificate_arn = module.frontend.acm_certificate_arn

  # lambda invoke arns
  lambda_list_invoke_arn        = module.lambda.lambda_list_invoke_arn
  lambda_get_invoke_arn         = module.lambda.lambda_get_invoke_arn
  lambda_put_invoke_arn         = module.lambda.lambda_put_invoke_arn
  lambda_post_invoke_arn        = module.lambda.lambda_post_invoke_arn
  lambda_delete_invoke_arn      = module.lambda.lambda_delete_invoke_arn
  lambda_title_to_id_invoke_arn = module.lambda.lambda_title_to_id_invoke_arn
  deployed_at                   = timestamp()
}

module "lambda" {
  source            = "./lambda"
  api_execution_arn = module.api.api_execution_arn
}

module "content" {
  source = "./content"

  lambda_exec_iam_arn = module.lambda.lambda_exec_iam_arn
}

module "frontend" {
  source       = "./frontend"
  tags         = var.tags
  ssl_cert_arn = var.ssl_cert_arn
  domain_name  = var.domain_name
}

module "cors_main" {
  source  = "mewa/apigateway-cors/aws"
  version = "2.0.1"

  api      = module.api.aws_api_gateway_rest_api_id
  resource = module.api.aws_api_gateway_resource_main_id

  methods = ["GET", "POST"]
}

module "cors_blog" {
  source  = "mewa/apigateway-cors/aws"
  version = "2.0.1"

  api      = module.api.aws_api_gateway_rest_api_id
  resource = module.api.aws_api_gateway_resource_blog_id

  methods = ["GET", "POST", "PUT", "DELETE"]
}

# module "pipeline" {
#   source = "./pipeline"

# }





# module "api" {
#   source = "./api"

# }


