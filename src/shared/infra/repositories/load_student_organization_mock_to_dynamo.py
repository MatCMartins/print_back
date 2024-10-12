

import boto3
import dotenv
from src.shared.infra.repositories.student_organization_repository_dynamo import StudentOrganizationRepositoryDynamo
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.environments import Environments


def setup_dynamo_table():
    dynamo_table_name = "stu_org_mss_template-table"
    endpoint_url = "http://localhost:8000"
    print("Setting up DynamoDB table...")

    dynamo_client = boto3.client('dynamodb', endpoint_url=endpoint_url)
    print("DynamoDB client created")
    tables = dynamo_client.list_tables()['TableNames']

    if dynamo_table_name not in tables:
        print("Creating table...")
        dynamo_client.create_table(
            TableName=dynamo_table_name,
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                }

            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print("Waiting for table to be created...")
        dynamo_client.get_waiter('table_exists').wait(TableName=dynamo_table_name)

        print('Loading table...')

        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

        table = dynamodb.Table(dynamo_table_name)

        print("Adding counter to table")

        table.put_item(
            Item={
                'PK': 'COUNTER',
                'SK': 'COUNTER'
            }
        )

        print('Table "stu_org_mss_template-table" created!')

    else:
        print("Table already exists!")


def load_mock_to_local_dynamo():
    setup_dynamo_table()
    mock_repo = StudentOrganizationRepositoryMock()
    dynamo_repo = StudentOrganizationRepositoryDynamo()

    count = 0

    print('Loading mock data to dynamo...')
    for stu_org in mock_repo.stu_orgs:
        print(f"Loading stu_org {stu_org.stu_org_id} | {stu_org.name} to dynamo")
        dynamo_repo.create_stu_org(stu_org)
        count += 1

    print(f"{count} stu_orgs loaded to dynamo!")

def load_mock_to_real_dynamo():
    mock_repo = StudentOrganizationRepositoryMock()
    dynamo_repo = StudentOrganizationRepositoryDynamo()

    count = 0

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamo_table_name=Environments.get_envs().dynamo_table_name)

    print("Adding counter to table")

    table.put_item(
        Item={
            'PK': 'COUNTER',
            'SK': 'COUNTER',
        }
    )

    print('Loading mock data to dynamo...')
    for stu_org in mock_repo.stu_orgs:
        print(f"Loading stu_org {stu_org.stu_org_id} | {stu_org.name} to dynamo")
        dynamo_repo.create_stu_org(stu_org)
        count += 1

    print(f"{count} stu_orgs loaded to dynamo!")
    
if __name__ == '__main__':
    dotenv.load_dotenv()
    load_mock_to_local_dynamo()
