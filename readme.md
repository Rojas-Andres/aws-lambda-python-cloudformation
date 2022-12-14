# INSTALL

## SAM CLI

https://docs.amazonaws.cn/en_us/serverless-application-model/latest/developerguide/install-sam-cli.html

#### Windows

https://github.com/aws/aws-sam-cli/releases/latest/download/AWS_SAM_CLI_64_PY3.msi

# AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#### WINDOWS

https://awscli.amazonaws.com/AWSCLIV2.msi

# Install Docker


# First
sam deploy --guided --profile YOUR_PROFILE

# DEPLOY

sam build --use-container

sam deploy --profile YOUR_PROFILE --config-env YOUR_ENV


# Docker

aws ecr-public get-login-password --region us-east-1 --profile user_test | docker login --username AWS --password-stdin public.ecr.aws
docker build -t dependencies-project .
docker tag dependencies-project:latest public.ecr.aws/r3y2i1c7/dependencies_docker
docker push public.ecr.aws/r3y2i1c7/dependencies_docker