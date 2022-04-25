import boto3
import json
import pprint

ddb = boto3.client('dynamodb','us-east-1')

#create table with LSI and GSI

createTable = ddb.create_table(
		TableName = 'Patient',
		AttributeDefinitions = [
			{'AttributeName': 'Id', 'AttributeType': 'N'},
			{'AttributeName': 'Name', 'AttributeType': 'S'},
			{'AttributeName': 'Age', 'AttributeType': 'S'},
			{'AttributeName': 'DOB', 'AttributeType': 'S'},
			{'AttributeName': 'Problem', 'AttributeType': 'S'},
			{'AttributeName': 'Code', 'AttributeType': 'N'}
		],
		KeySchema = [
			{'AttributeName': 'Id', 'KeyType': 'HASH'},
			{'AttributeName': 'Name', 'KeyType': 'RANGE'}
		],
		ProvisionThroughput = {
			'ReadCapacityUnits': 5,
			'WriteCapacityUnits': 5
		},
		LocalSecondaryIndexes = [
			{
				'IndexName': 'PatientLSIx1',
				'KeySchema': [
					{'AttributeName': 'Id', 'KeyType': 'HASH'},
					{'AttributeName': 'Age', 'KeyType': 'RANGE'}
				],
				'Projection':{
					'ProjectionType': 'KEYS_ONLY'
				}
			},
			{
				'IndexName': 'PatientLSIx2',
				'KeySchema': [
					{'AttributeName': 'Id', 'KeyType': 'HASH'},
					{'AttributeName': 'Problem', 'KeyType': 'RANGE'}
				],
				'Projection':{
					'ProjectionType': 'KEYS_ONLY'
				}
			}
		],
		GlobalSecondaryIndexes = [
			{
				'IndexName': 'PatientGSIx1',
				'KeySchema': [
					{'AttributeName': 'Code', 'KeyType': 'HASH'},
					{'AttributeName': 'DOB', 'KeyType': 'RANGE'}
				],
				'Projection':{
						'ProjectionType': 'KEYS_ONLY'
				},
				'ProvisionThroughput': {
					'ReadCapacityUnits': 5,
					'WriteCapacityUnits': 5
				}
			},
		]
)
pprint(createTable)
