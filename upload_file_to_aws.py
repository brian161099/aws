
# %%
import boto3

# Credentials: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
s3 = boto3.resource('s3')

BUCKET = "bookkeeping-financial-data"

file_name = "credit_card_bin.xlsx"

s3.Bucket(BUCKET).upload_file(file_name, f"direct_upload_to_s3/{file_name}")
