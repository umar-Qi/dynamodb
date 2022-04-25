import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movie')

with open('source.json') as json_file:
	movies = json.load(json_file, parse_float = decimal.Decimal)
	For movie in movies:
		year = int(x['year'])
		title = x['title']
		rating = x['rating']
		
		#print('adding movies',year,title)
		
		table.put_item(
			Item={
				'year':year,
				'title':title,
				'rating':decimal.Decimal(6.7)
			}
		)
