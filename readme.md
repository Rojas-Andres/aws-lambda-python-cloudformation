# INSTALL

## SAM CLI

- https://docs.amazonaws.cn/en_us/serverless-application-model/latest/developerguide/install-sam-cli.html

#### Windows

- https://github.com/aws/aws-sam-cli/releases/latest/download/AWS_SAM_CLI_64_PY3.msi

# AWS CLI
- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#### WINDOWS

https://awscli.amazonaws.com/AWSCLIV2.msi

# Install Docker


# First
- sam deploy --guided --profile YOUR_PROFILE

# DEPLOY

- sam build --use-container

- sam deploy --profile YOUR_PROFILE --config-env YOUR_ENV

- sam deploy --profile user_test --config-env develop

# Sam build default
https://gallery.ecr.aws/sam/build-python3.9

# Repository 
https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html

# start api
https://docs.aws.amazon.com/es_es/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html

# Docker

- aws ecr-public get-login-password --region us-east-1 --profile user_test | docker login --username AWS --password-stdin public.ecr.aws

- docker build -t dependencies-project .

- docker tag dependencies-project:latest public.ecr.aws/r3y2i1c7/dependencies_docker

- docker push public.ecr.aws/r3y2i1c7/dependencies_docker

# Correr proyecto local
- sam local start-api --invoke-image public.ecr.aws/r3y2i1c7/dependencies_docker
# Correr con parametros 
 sam local start-api --invoke-image public.ecr.aws/r3y2i1c7/dependencies_docker --parameter-overrides $(cat .sam-params)


# Crear tabla usuarios

create table users(
	id serial,
	"name" varchar(250),
	last_name varchar(250),
	city varchar(250),
	"password" varchar(250),
	email varchar(250)
)