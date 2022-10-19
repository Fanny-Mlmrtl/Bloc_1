import json
import os
import pandas as pd
import boto3
import csv

AWSAccessKeyId='AKIA3HBJJFOXIKPYVD26'
AWSSecretKey='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'

session = boto3.Session(aws_access_key_id=AWSAccessKeyId,
                        aws_secret_access_key=AWSSecretKey)

s3 = session.resource("s3")

#bucket = s3.create_bucket(Bucket="kayak-project-fm", CreateBucketConfiguration={'LocationConstraint': 'eu-west-3'})

s3.Bucket('kayak-project-fm').upload_file('C:/Users/fanny/Documents/Jedha/Kayak/complete_h_w.csv', 'complete_h_w.csv')
s3.Bucket('kayak-project-fm').upload_file('C:/Users/fanny/Documents/Jedha/Kayak/top_destinations_h_w.csv', 'top_destinations_h_w.csv')
