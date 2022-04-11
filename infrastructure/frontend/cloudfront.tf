resource "aws_cloudfront_origin_access_identity" "main" {
  comment = "Frontend cloudfront identity access for ${var.tags["Name"]}"
}

locals {
  s3_origin_id          = "${var.tags["Name"]}-s3-origin"
  s3_origin_id_redirect = "${var.tags["Name"]}-s3-origin-redirect"
}


resource "aws_cloudfront_distribution" "main" {
  origin {

    # ------- Works here ----------
    # 
    domain_name = aws_s3_bucket.main.bucket_domain_name
    origin_id   = local.s3_origin_id
    # 
    # --------- Works here ----------

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  comment             = "${var.tags["Name"]} main distribution"
  default_root_object = "index.html"

  aliases = ["${var.domain_name}"]

  default_cache_behavior {
    response_headers_policy_id = aws_cloudfront_response_headers_policy.main.id
    allowed_methods            = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods             = ["GET", "HEAD", "OPTIONS"]
    target_origin_id           = local.s3_origin_id

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  # price_class = "PriceClass_200"

  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate.main.arn
    ssl_support_method  = "sni-only"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  custom_error_response {
    error_code         = 403
    response_page_path = "/index.html"
    response_code      = 200
  }
}

resource "aws_cloudfront_response_headers_policy" "main" {
  name = "${var.tags["Name"]}-cloudfront-header-policy"

  cors_config {
    access_control_allow_credentials = false

    access_control_allow_headers {
      items = ["*"]
    }

    access_control_allow_methods {
      items = ["ALL"]
    }

    access_control_allow_origins {
      items = ["*"]
    }

    origin_override = true
  }
}

resource "aws_cloudfront_distribution" "redirect" {
  origin {

    # ------- Error here ----------
    # 
    # Manual configuration in AWS console to this value works as expected
    # eg. DOC-EXAMPLE-BUCKET.s3-website-us-east-1.amazonaws.com
    # 
    # domain_name = aws_s3_bucket_website_configuration.redirect.website_endpoint
    # 
    # --------- Error here ----------

    domain_name = aws_s3_bucket.redirect.bucket_domain_name

    origin_id = local.s3_origin_id_redirect




    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path
    }
  }

  enabled         = true
  is_ipv6_enabled = true
  comment         = "${var.tags["Name"]} redirect distribution"

  aliases = ["www.${var.domain_name}"]

  default_cache_behavior {
    response_headers_policy_id = aws_cloudfront_response_headers_policy.main.id
    allowed_methods            = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods             = ["GET", "HEAD", "OPTIONS"]
    target_origin_id           = local.s3_origin_id_redirect

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  # price_class = "PriceClass_200"

  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate.main.arn
    ssl_support_method  = "sni-only"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
}
