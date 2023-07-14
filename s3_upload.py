import boto3

def s3_upload(filePath, newFileName):
    s3 = boto3.resource("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    bucketName = "elasticbeanstalk-ap-northeast-1-364557162645"
    with open(filePath, 'rb') as data:
        s3.Bucket(bucketName).upload_fileobj(data, 'uploads/' + newFileName)
    return newFileName