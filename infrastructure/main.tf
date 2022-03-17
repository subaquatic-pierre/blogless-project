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
  source                     = "./api"
  lambda_list_all_invoke_arn = module.lambda.lambda_list_all_invoke_arn
  domain_name                = var.domain_name
  acm_certificate_arn        = module.frontend.acm_certificate_arn
}

module "lambda" {
  source            = "./lambda"
  api_execution_arn = module.api.api_execution_arn
}

module "content" {
  source = "./content"
}

module "frontend" {
  source       = "./frontend"
  tags         = var.tags
  ssl_cert_arn = var.ssl_cert_arn
  domain_name  = var.domain_name
}

# module "pipeline" {
#   source = "./pipeline"

# }





# module "api" {
#   source = "./api"

# }


