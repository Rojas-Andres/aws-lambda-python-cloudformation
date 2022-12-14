FROM public.ecr.aws/sam/emulation-python3.9:latest

COPY ./modules/users/requirements.txt ./modules/users/requirements.txt

RUN pip install -r ./modules/users/requirements.txt