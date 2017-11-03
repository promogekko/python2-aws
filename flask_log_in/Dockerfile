FROM centos:7
MAINTAINER dockerlite@gmail.com

RUN yum -y update && \
    yum -y install git tar unzip wget python-pip 

ADD requirement.txt /

RUN pip install -r requirement.txt


