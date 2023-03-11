import boto3
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], 'f:b:d:', ["key=", "secret=", "file=", "bucket=", "destination="])
for opt, arg in opts:
    if opt in ("-f", "--file"):
        file = arg
    
    elif opt in ("-b", "--bucket"):
        bucket = arg
    
    elif opt in ("-d", "--destination"):
        destination = arg

client = boto3.client("s3")
client.upload_file(file, bucket, destination)