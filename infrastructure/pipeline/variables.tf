variable "aws_account_id" {}
variable "prefix" {}
variable "frontend_site_bucket" {}
variable "frontend_cf_distribution" {}
variable "tags" {}

variable "github_account" {}
variable "github_repo" {}
variable "codestar_connection" {}

variable "build_secrets" {
  type        = map(string)
  description = "All secrets used in building images"
}

variable "codebuild_role" {}
variable "codepipeline_role" {}

