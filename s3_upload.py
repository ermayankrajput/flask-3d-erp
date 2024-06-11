import boto3
import os.path

def s3_upload(filePath, newFileName):
    s3 = boto3.resource("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    bucketName = "elasticbeanstalk-ap-northeast-1-364557162645"
    with open(filePath, 'rb') as data:
        s3.Bucket(bucketName).upload_fileobj(data,  newFileName)
    return newFileName

def downloadFile(filePath,path):
    # s3 = boto3.resource("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    # bucketName = "elasticbeanstalk-ap-northeast-1-364557162645"
    # s3.Bucket.download_file('elasticbeanstalk-ap-northeast-1-364557162645', filePath, 'hello2.txt')
    s3 = boto3.client("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    # breakpoint()
    if not os.path.isfile(path+'/'+filePath.split("/")[-1]):
        s3.download_file('elasticbeanstalk-ap-northeast-1-364557162645', filePath, path+'/'+filePath.split("/")[-1])
    # s3.download_file('elasticbeanstalk-ap-northeast-1-364557162645', filePath, filePath)
    # s3.Bucket(bucketName).download_file(filePath)
