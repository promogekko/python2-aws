#! /usr/bin/python

import boto3

#----------------------------------------------------------------
#create une ressource S3
s3 = boto3.resource('s3')

#print(type(s3))

# list des buckets
for bucket in s3.buckets.all():
   print bucket.name

# creer un S3 client pour creer un bucket
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='51.255.211.214-mybucket')

# ajouter une imaged
data = open('test.jpg', 'rb')
s3.Bucket('51.255.211.214-mybucket').put_object(Key="test.jpg",Body=data)

#------------------------------------------------------------------------------

