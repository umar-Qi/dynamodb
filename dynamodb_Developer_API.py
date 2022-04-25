import boto3
import pprint
import json
import decimal
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movie')

#############################		
# Insert an item into table
#############################

year = '2015'
title = 'galaxy'
		
	response = table.put_item(
			Item={
				'year':year,
				'title':title,
				'rating':decimal.Decimal(6.7)
			}
		)
		
print("put item succeeded")
pprint.pprint(response)

################################
# Read a single item from table
################################

year = '2010'
title = 'avatar'

try:
	response = table.get_item(
		key = {
			'year':year,
			'title':title
		}
		ProjectionExpression = "title,year,...." #optional, this for filtering result
	)
except ClientError as e:
	print(e.response['Error']['Message'])
else:
	item : response['Item']
	print("GetItem succeeded: ")
	pprint.pprint(response['Item'])
	
###########################################
# Query to get a range of items from table
###########################################

print("movies from 1999")

response = table.query(
	KeyConditionExpression = Key('year').eq(1999)
	ProjectionExpression = "title,info.image,...." #optional, this for filtering result
	ConsistentRead = True,				#optional | by default false | use for data consistency
	ReturnConsumedCapacity = 'Total'
)

pprint.pprint(response)

for i in reposnse['items']:	#optional for printing only two attributes
	print(i['year'], ":", i['title']) 
	
###########################################
# Query to get a single item from table
##########################################

print("movies from 2010 - titles A-G with genres and lead actors")

response = table.query(
	ProjectionExpression = "#yr, title, info.genres, info.actors[0]",
	ExpressionattributeNames = {"#yr":"year"},
	KeyConditionExpression = Key('year').eq(2010) & Key('title').between('A','G')
)

pprint.pprint(response)

########################################
# Scan the entire table
########################################

year_range = Key('year').between(2001,2010)
project = "#yr, title, info.rating"
# Expression Attribute Names for Projection Expression only
expr = {"#yr": "year"}

response = table.scan(
	FilterExpression = Key('year').between(2001,2010),
	ProjectionExpression = project,
	ExpressionAttributeNames = expr
)

pprint.pprint(response['Items'])
