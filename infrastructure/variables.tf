variable "aws_account_id" {
  type        = string
  description = "AWS account if to be used in pipeline"
}
variable "github_account" {
  type        = string
  description = "Github account name associated with frontent repo"
}

# ------
# Repositories
# ------
variable "github_repo" {
  type        = map(string)
  description = "Repo with frontend code"
}

variable "tags" {
  type        = map(string)
  description = "Tags to be used in the project"
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

variable "build_secrets" {
  type        = map(string)
  description = "Build secrets to be used in build pipeline"
}




