FROM centos:7
MAINTAINER dockerlite@gmail.com

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install git tar unzip wget python-pip mysql && \
    python -m pip install -U pip && \
    yum clean all

ADD requirements.txt /

RUN pip install -r /requirements.txt

RUN git clone https://github.com/promogekko/Flask-Login.git

WORKDIR /Flask-Login

EXPOSE 5000

ENTRYPOINT ["python","app.py","runserver"]

CMD ["-h=0.0.0.0"]



