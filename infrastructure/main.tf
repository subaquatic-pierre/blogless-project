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

module "lambda" {
  source = "./lambda"
}

# module "pipeline" {
#   source = "./pipeline"

# }

# module "frontend" {
#   source = "./frontend"

# }



# module "api" {
#   source = "./api"

# }


