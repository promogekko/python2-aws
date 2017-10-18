#! /usr/bin/python

import boto3
import datetime
import glob
import os

web_log ="/var/log/centos-web/"
mysql_log="/var/log/mysql-db/"

# get S3 resource
s3 = boto3.resource('s3')

# create a web log bucket
s3_client = boto3.client('s3')

#-------- web log files ----------------------
web_file = os.listdir(web_log)
weblog_bucket_name = datetime.datetime.now().strftime('weblog_%d_%m_%Y_%H_%M')

s3_client.create_bucket(Bucket=weblog_bucket_name)


for log_file in web_file: 
    # write a bucket 
    ft= web_log + log_file
    data = open(ft, 'rb')
    s3.Bucket(weblog_bucket_name).put_object(Key=log_file ,Body=data)

#------- mysql log file ------------------------
mysql_file = os.listdir(mysql_log)
mysql_bucket_name = datetime.datetime.now().strftime('mysqllog_%d_%m_%Y_%H_%M')

s3_client.create_bucket(Bucket=mysql_bucket_name)

for log_file in mysql_file:
    # write a bucket
    ft= mysql_log + log_file
    data = open(ft, 'rb')
    s3.Bucket(mysql_bucket_name).put_object(Key=log_file ,Body=data)

