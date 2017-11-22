#! /usr/bin/python

from os.path import expanduser
import boto3
import datetime
import os
import netrc

machine = "db"
info = netrc.netrc().authenticators(machine) 
command = "/usr/bin/docker exec  python2aws_db_1 /usr/bin/mysqldump -u {} --password={} BucketList tbl_user >tbl_user.sql".format(info[0],info[2])
os.system(command)
path = os.getcwd()
#path = expanduser("~")


# get S3 resource
s3 = boto3.resource('s3')

# create a web log bucket
s3_client = boto3.client('s3')

#-------- web log files ----------------------
backup_bucket_name = datetime.datetime.now().strftime('backup_%d_%m_%Y_%H_%M')
s3_client.create_bucket(Bucket=backup_bucket_name)

ft = path + "/"  + "tbl_user.sql"
data = open(ft, 'rb')
s3.Bucket(backup_bucket_name).put_object(Key="tbl_user.sql" ,Body=data)


