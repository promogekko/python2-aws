FROM centos:7
MAINTAINER dockerlite@gmail.com

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install git tar unzip wget python-pip && \
    python -m pip install -U pip && \
    yum clean all

ADD requirements.txt /

RUN pip install -r /requirements.txt


