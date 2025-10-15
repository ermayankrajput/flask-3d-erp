import boto3
import os.path
import requests
import os

def s3_upload(filePath, newFileName):

    # s3 = boto3.resource("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    # bucketName = "elasticbeanstalk-ap-northeast-1-364557162645"
    # with open(filePath, 'rb') as data:
    #     s3.Bucket(bucketName).upload_fileobj(data,  newFileName)
    # return newFileName
    url = "https://phpstack-1502240-5925329.cloudwaysapps.com/upload.php"
    secret = "YOUR_SECRET_KEY"

    # Derive relative path (after your base upload folder if needed)
    relative_path = os.path.normpath(filePath).replace("\\", "/")
    relative_path = os.path.basename(relative_path) if relative_path.startswith("/") else relative_path

    # Example: /Users/nitin/Desktop/uploads/products/2025/item.jpg → uploads/products/2025/item.jpg
    # You can trim local prefix if needed:
    # relative_path = relative_path.split("uploads/")[-1]

    with open(filePath, 'rb') as f:
        files = {'file': f}
        data = {'filePath': relative_path, 'key': secret}
        response = requests.post(url, data=data, files=files)

    data = response.json()
    if 'url' in data:
        print(f"✅ Uploaded: {data['url']}")
        return data['url']
    else:
        raise Exception(f"❌ Upload failed: {data.get('error')}")

def s3_delete(filename):
    url = "https://phpstack-1502240-5925329.cloudwaysapps.com/delete.php"
    data = {
        'key': 'YOUR_SECRET_KEY',
        'filename': filename
    }
    response = requests.post(url, data=data)
    result = response.json()
    if result.get('success'):
        print("✅ File deleted:", filename)
        return True
    else:
        print("❌ Error:", result.get('error'))
        return False

def downloadFile(filePath,path):
    # If filePath is relative, build full URL
    if not filePath.startswith('https'):
        base_url = "https://phpstack-1502240-5925329.cloudwaysapps.com/files/"
        file_url = base_url + filePath.lstrip('/')
    else:
        file_url = filePath
    os.makedirs(path, exist_ok=True)
    filename = os.path.basename(file_url)
    local_path = os.path.join(path, filename)

    if os.path.isfile(local_path):
        print(f"✅ File already exists: {local_path}")
        return local_path

    print(f"⬇️ Downloading {filename} from {file_url}...")

    try:
        with requests.get(file_url, stream=True) as response:
            response.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"✅ Download complete: {local_path}")
        return local_path

    except Exception as e:
        print(f"❌ Download failed for {file_url}: {e}")
        raise
    # # s3 = boto3.resource("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    # # bucketName = "elasticbeanstalk-ap-northeast-1-364557162645"
    # # s3.Bucket.download_file('elasticbeanstalk-ap-northeast-1-364557162645', filePath, 'hello2.txt')
    # s3 = boto3.client("s3", aws_access_key_id="AKIAVJYKM3CKTXR2RUTW", aws_secret_access_key= "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")
    # # breakpoint()
    # if not os.path.isfile(path+'/'+filePath.split("/")[-1]):
    #     s3.download_file('elasticbeanstalk-ap-northeast-1-364557162645', filePath, path+'/'+filePath.split("/")[-1])
    # # s3.download_file('elasticbeanstalk-ap-northeast-1-364557162645', filePath, filePath)
    # # s3.Bucket(bucketName).download_file(filePath)
