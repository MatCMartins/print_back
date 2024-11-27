#!/usr/bin/env python3
import os
import logging
import aws_cdk as cdk
from adjust_layer_directory import adjust_layer_directory
from iac.iac_stack import IacStack  # Atualize o caminho conforme necessário

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Starting the CDK application")

try:
    logging.info("Adjusting the layer directory")
    adjust_layer_directory(shared_dir_name="shared", destination="lambda_layer_out_temp")
    logging.info("Finished adjusting the layer directory")
except Exception as e:
    logging.error(f"Failed to adjust the layer directory: {e}")
    exit(1)

app = cdk.App()

aws_region = os.environ.get("AWS_REGION")
aws_account_id = os.environ.get("AWS_ACCOUNT_ID")
stack_name = os.environ.get("STACK_NAME")

if not aws_region or not aws_account_id or not stack_name:
    logging.error("One or more required environment variables are missing: AWS_REGION, AWS_ACCOUNT_ID, STACK_NAME")
    exit(1)

# Determinar o estágio com base no nome da stack
if 'prod' in stack_name.lower():
    stage = 'PROD'
elif 'homolog' in stack_name.lower():
    stage = 'HOMOLOG'
elif 'dev' in stack_name.lower():
    stage = 'DEV'
else:
    stage = 'TEST'

tags = {
    'project': 'Template',
    'stage': stage,
    'stack': 'BACK',
    'owner': 'LCStuber'
}

logging.info(f"Creating the stack with name: {stack_name} in stage: {stage}")
try:
    IacStack(
        app,
        stack_name,
        env=cdk.Environment(account=aws_account_id, region=aws_region),
        tags=tags
    )
    logging.info("Stack created successfully")
except Exception as e:
    logging.error(f"Failed to create the stack: {e}")
    exit(1)

app.synth()
