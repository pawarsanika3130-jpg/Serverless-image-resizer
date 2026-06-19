import boto3
from PIL import Image
import os

s3 = boto3.client('s3')

DEST_BUCKET = 'imag-resized-bucket-1'  # Change to your bucket name

def lambda_handler(event, context):

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    filename = os.path.basename(object_key)

    download_path = f"/tmp/{filename}"
    resized_path = f"/tmp/resized-{filename}"

    s3.download_file(source_bucket, object_key, download_path)

    with Image.open(download_path) as image:
        image.thumbnail((300, 300))
        image.save(resized_path)

    s3.upload_file(
        resized_path,
        DEST_BUCKET,
        f"resized-{filename}"
    )

    return {
        "statusCode": 200,
        "body": "Image resized successfully"
    }
