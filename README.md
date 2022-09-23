# Serverless Blog

The project features full serverless blog hosted handled by AWS services.

## Usage

1. Clone the repo
2. Ensure your have a AWS account
3. Ensure your have Terraform installed
4. Configure Terraform with AWS credentials for region us-east-1
5. Initialize terraform backend
6. Rename 'terraform.tfvars.example' to 'terraform.tfvars', edit file with your credentials

```
    terraform init

```

7. Apply terraform

```
    terraform apply
```

8. Check your endpoints

## Notes

- You may need to apply terraform more than once as creating certificates and cloudfronts can take time and may not work the first time. Try 2 or 3 terraform apply commands, it should work

## Endpoints

### Frontend

Domain Name: www.yourdomain.com / yourdomain.com

| Endpoint | Method | Description              |
| -------- | ------ | ------------------------ |
| /        | GET    | Home page of the website |

### API

Domain Name: api.yourdomain.com

| Endpoint   | Method | Description                 |
| ---------- | ------ | --------------------------- |
| /blog      | GET    | List all blogs              |
| /blog      | POST   | Create new blog             |
| /blog/{id} | GET    | Get details of blog with ID |
| /blog/{id} | PUT    | Update blog with given ID   |
| /blog/{id} | DELETE | Delete blog with ID         |

### Technologies

#### AWS Services

- Cloudfront
- S3
- Lambda
- Route53

#### Infrastructure

All infrastructure is Infrastructure as Code with TerraForm

#### API

The lambda API functions are written in Python

#### Frontend

The frontend is written using the React Framework.

```

```
