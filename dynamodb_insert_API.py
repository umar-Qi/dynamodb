import boto3
import json

dynamodb = boto3.client('dynamodb','us-east-1')

#insert data from json file into dynamodb table
with open('data-file.json','r') as input_file:
	for record in input_file:
		empid = str(json.loads(record)['id'])
		fname = json.loads(record)['name']['first_name']
		lname = json.loads(record)['name']['last_name']
		email = json.loads(record)['email']
		tech = json.loads(record)['technology']
		print(fname,lname)
		
		try:
			put_data = dynamodb.put_item(TableName='DB-emp',
							Item={
								'empid' : {'N' : empid},
								'Name' : {'M' : {'fname' :{'S':fname},'lname':{'S':lname}}},
								'email' : {'S': email},
								'Technology' : {'SS' : tech}
							}
							)
							
		except Exception as e:
			print("Error! Unable to put record is Dynamodb Table", record)
			print(e)
		else:
			print("put successful")


