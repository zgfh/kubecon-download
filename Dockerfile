FROM python:3.6-stretch

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

ADD requirements.txt requirements.txt
RUN pip install  -i https://mirrors.aliyun.com/pypi/simple --upgrade pip ;pip install -r requirements.txt ;
ADD . .
CMD ["python", "kubecon.py"]