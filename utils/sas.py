import boto3

opts, args = getopt.getopt(sys.argv[1:], 'k:s:f:b:d:', ["key=", "secret=", "file=", "bucket=", "destination="])
for opt, arg in opts:
    if opt in ("-k", "--key"):
        key = arg

    elif opt in ("-s", "--secret"):
        secret = arg

    elif opt in ("-f", "--file"):
        file = arg
    
    elif opt in ("-b", "--bucket"):
        bucket = arg
    
    elif opt in ("-d", "--destination"):
        destination = arg

client = boto3.client("s3")
client.upload_file(file, bucket, destination)