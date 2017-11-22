#! /usr/bin/python

import boto3

# get S3
# resource
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# list des buckets
for bucket in s3.buckets.all():
   print bucket.name
   bucket = s3.Bucket(bucket.name)
   bucket.objects.all().delete()
   for obj in bucket.objects.all():
       obj.delete()
   bucket.delete()
