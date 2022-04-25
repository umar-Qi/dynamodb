import boto3
import json
import pprint

ddb = boto3.client('dynamodb','us-east-1')

#updating few things in table like(change the RCU and WCU of table and also adding an attribute)

updateTable = ddb.update_table(
	TableName = 'Patient',
	ProvisionThroughput = {
		'ReadCapacityUnits':3,
		'WriteCapacityUnits':3
	},
	AttributeDefinitions = {
		'AttributeName': 'diagnosis',
		'AttributeType': 'S'
	}
)

#adding a GSI index in table

updateTable = ddb.update_table(
	TableName = 'Patient',
	AttributeDefinitions = {
		'AttributeName': 'diagnosis',
		'AttributeType': 'S'
	}
	GlobalSecondaryIndexUpdates = [
		{
			'create': {
				'IndexName': 'PatientGSIx2',
				'KeySchema': [
					{'AttributeName': 'disgnosis', 'KeyType': 'RANGE'},	
				],
				'Projection': {
					'ProjectionType': 'KEYS_ONLY'
				},
				'ProvisionThroughput': {
					'ReadCapacityUnits': 2,
					'WriteCapacityUnits': 2
				}
			}
		}
	]
)

#updating RCU and WCU of any GSI

updateTable = ddb.update_table(
	TableName = 'Patient',
	GlobalSecondaryIndexUpdates = [
		{
			'update': {
				'IndexName': 'PatientGSIx1',
				'ProvisionThroughput':{
					'ReadCapacityUnits': 3,
					'WriteCapacityUnits': 3
				}
				
			}	
		}
	]
)

#deleting a GSI index

updateTable = ddb.update_table(
	TableName = 'Patient',
	GlobalSecondaryIndexUpdates = [
		{
			'delete': {
				'IndexName': 'PatientGSIx1'
			}
		}
	]
)
