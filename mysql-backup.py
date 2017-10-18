#! /usr/bin/python

import boto3
import datetime
import os
import netrc

machine = "db"
info = netrc.netrc().authenticators(machine) 
command = "docker exec  centos_db_1 /usr/bin/mysqldump -u {} --password={} test >test-db.sql".format(info[0],info[2])
os.system(command)
path = os.getcwd()


# get S3 resource
s3 = boto3.resource('s3')

# create a web log bucket
s3_client = boto3.client('s3')

#-------- web log files ----------------------
backup_bucket_name = datetime.datetime.now().strftime('backup_%d_%m_%Y_%H_%M')
s3_client.create_bucket(Bucket=backup_bucket_name)

ft = path + "/"  + "test-db.sql"
data = open(ft, 'rb')
s3.Bucket(backup_bucket_name).put_object(Key="test-db.sql" ,Body=data)


