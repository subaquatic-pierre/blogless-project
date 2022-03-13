data "aws_route53_zone" "main" {
  name         = var.domain_name
  private_zone = false
}

resource "aws_route53_record" "main" {
  zone_id         = data.aws_route53_zone.main.id
  name            = var.domain_name
  type            = "A"
  allow_overwrite = true

  alias {
    name                   = aws_cloudfront_distribution.frontend_main.domain_name
    zone_id                = aws_cloudfront_distribution.frontend_main.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "www" {
  zone_id         = data.aws_route53_zone.main.id
  name            = "www.${var.domain_name}"
  type            = "A"
  allow_overwrite = true

  alias {
    name                   = aws_cloudfront_distribution.frontend_redirect.domain_name
    zone_id                = aws_cloudfront_distribution.frontend_redirect.hosted_zone_id
    evaluate_target_health = false
  }
}
