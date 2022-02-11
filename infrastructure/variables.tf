variable "aws_account_id" {}
variable "github_account" {}

# ------
# Repositories
# ------
variable "github_repo" {
  type        = map(string)
  description = "Repo with frontend code"
}

# ------
# Domain Variables
# ------

variable "domain_name" {
  type        = string
  description = "Root Route53 domain name"
}

variable "ssl_cert_arn" {
  type        = string
  description = "ARN of the certificate covering the fqdn and its apex?"
}

# ------
# VPC Variables
# ------
variable "vpc_cidr" {}



