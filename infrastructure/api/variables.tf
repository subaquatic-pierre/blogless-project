variable "acm_certificate_arn" {}
variable "acm_certificate_domain_name" {}

variable "rest_api_domain_name" {
  default     = "scubadivedubai.com"
  description = "Domain name of the API Gateway REST API for self-signed TLS certificate"
  type        = string
}

variable "rest_api_name" {}
variable "rest_api_path" {}
