# AWS Serverless Image Resizer

## Overview

This project automatically resizes images uploaded to an Amazon S3 bucket using AWS Lambda and Pillow. The resized images are stored in a separate S3 bucket.

## Architecture

User Uploads Image → Amazon S3 → S3 Event Trigger → AWS Lambda → Pillow Image Processing → Amazon S3 Output Bucket

## AWS Services Used

* AWS Lambda
* Amazon S3
* AWS IAM
* Amazon CloudWatch

## Features

* Automatic image resizing
* Event-driven architecture
* Fully serverless
* Scalable and cost-effective

## Workflow

1. Upload an image to the source S3 bucket.
2. S3 triggers the Lambda function.
3. Lambda downloads the image.
4. Pillow resizes the image.
5. Resized image is uploaded to the destination S3 bucket.

## Technologies

* Python 3.13
* AWS Lambda
* Amazon S3
* Pillow

## Author

Vedantika Pawar
