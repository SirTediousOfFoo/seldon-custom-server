import boto3

s3_region = '' # fill in for AWS, blank for Ceph
s3_endpoint_url = 'https://url-do-storagea.com/'
s3_access_key_id = 'access_key'
s3_secret_access_key = 'access_secret'
s3_bucket = 'aiops-test-bucket'

# configure boto S3 connection
s3 = boto3.client('s3',
                  s3_region,
                  endpoint_url = s3_endpoint_url,
                  aws_access_key_id = s3_access_key_id,
                  aws_secret_access_key = s3_secret_access_key,
                  verify=False)

#upload the file to storage
s3.upload_file("./simpleLinearRegression", s3_bucket, "regression.joblib")