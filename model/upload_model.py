s3_region = '' # fill in for AWS, blank for Ceph
s3_endpoint_url = 'https://s3-openshift-storage.apps.dos-cloud.lan.croz.net/'
s3_access_key_id = 'Tx1HnuJLLX575v1CL94P'
s3_secret_access_key = 'y/kUAStrFIX0AOAabOqTj/TBw+rQ9h9xuhb71BwD'
s3_bucket = 'aiops-test-bucket'

import boto3

# configure boto S3 connection
s3 = boto3.client('s3',
                  s3_region,
                  endpoint_url = s3_endpoint_url,
                  aws_access_key_id = s3_access_key_id,
                  aws_secret_access_key = s3_secret_access_key,
                  verify=False)

#upload the file to storage
s3.upload_file("./simpleLinearRegression", s3_bucket, "regression.joblib")