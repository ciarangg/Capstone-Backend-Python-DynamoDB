import boto3
import decimal
import json



from src.client_factory import DynamoDBClient
from src.dynamodb import DynamoDB

def get_dynamodb_resource():
    dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
    """ :type : pyboto3.dynamodb """
    return dynamodb


def get_dynamodb():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)
    return dynamodb

def create_dynamodb_table():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)

    table_name = "post"

    attribute_definitions = [
         {
             'AttributeName': 'title',
             'AttributeType': 'S'
         },
         {
             'AttributeName': 'content',
             'AttributeType': 'S'
         }
     ]

    key_schema = [
        {
            'AttributeName': 'content',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }

    dynamodb_create_table_response = dynamodb.create_table(table_name, attribute_definitions, key_schema, initial_iops)
    print("Created DynamoDB Table named " + table_name + ":" + str(dynamodb_create_table_response))

def create_dynamodb_table_user():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)

    table_name = "user"

    attribute_definitions = [
         {
             'AttributeName': 'username',
             'AttributeType': 'S'
         }
     ]

    key_schema = [
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }

    dynamodb_create_table_response = dynamodb.create_table(table_name, attribute_definitions, key_schema, initial_iops)
    print("Created DynamoDB Table named " + table_name + ":" + str(dynamodb_create_table_response))

def insert_sample_data_user():
    table = get_dynamodb_resource().Table("user")

    with open("userdata.json") as json_file:
        users = json.load(json_file, parse_float=decimal.Decimal)
        for user in users:
            username = user['username']

            print("Adding post:", username)

            table.put_item(
                Item={
                    'username': username
                }
            )

    print("Sample user data inserted successfully!")


def describe_table():
    print(str(get_dynamodb().describe_table("post")))


def update_table_iops():
    get_dynamodb().update_read_write_capacity("post", 15, 15)


def delete_table():
    get_dynamodb().delete_table_with_name("post")

def insert_sample_data():
    table = get_dynamodb_resource().Table("post")

    with open("postdata.json") as json_file:
        posts = json.load(json_file, parse_float=decimal.Decimal)
        for post in posts:
            title = post['title']
            content = post['content']

            print("Adding post:", title, content)

            table.put_item(
                Item={
                    'title': title,
                    'content': content,
                }
            )

    print("Sample post data inserted successfully!")

def get_item_on_table():
    try:
        response = get_dynamodb_resource().Table("post").get_item(
            Key={
                    'title': "My GC Machine isn't working",
                    'content': "It's been working all year and last month my sample results are off by 70%"
            }
        )
    except ClientError as error:
        print(error.response['Error']['Message'])
    else:
        item = response['Item']
        print("Got the item successfully!")
        print(str(response))

def put_item_on_table():
    try:
        response = get_dynamodb_resource().Table("post").put_item(
            Item={
                'title': "Blarp",
                'content': "Blarp",
                'info': "some random stuff"
            }
        )

        print("A New Post added to the collection successfully!")
        print(str(response))
    except Exception as error:
        print(error)

def update_item_on_table():
    response = get_dynamodb_resource().Table("post").update_item(
        Key={
                'title': "Blarp",
                'content': "Blarp"
        },
        UpdateExpression="set info = :i",
        ExpressionAttributeValues={
            ':i': "lets change the info"
        },
        ReturnValues="UPDATED_NEW"
    )

    print("Updating existing post was success!")
    print(str(response))

def delete_item_on_table():
    try:
        response = get_dynamodb_resource().Table("post").delete_item(
            Key={
                'title': "Blarp",
                'content': "Blarp",
            }
            )
    except ClientError as error:
        if error.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(error.response['Error']['Message'])
        else:
            raise
    else:
        print("Deleted item successfully!")
        print(str(response))






if __name__ == '__main__':
    # create_dynamodb_table()
    # insert_sample_data()
    # describe_table()
    # update_table_iops()
    # delete_table()
    # get_item_on_table()
    # put_item_on_table()
    # update_item_on_table()
    # delete_item_on_table()
    create_dynamodb_table_user()
    # insert_sample_data_user()




# import boto3
# import decimal
# import json
#
# def get_dynamodb_client():
#     dynamodb = boto3.client("dynamodb", region_name="us-west-2", endpoint_url="http://localhost:8000")
#     """ :type : pyboto3.dynamodb """
#     return dynamodb
#
# def get_dynamodb_resource():
#     dynamodb = boto3.resource("dynamodb", region_name="us-west-2", endpoint_url="http://localhost:8000")
#     """ :type : pyboto3.dynamodb """
#     return dynamodb
#
# def create_table():
#     table_name = "posts"
#
#     attribute_definitions = [
#         {
#             'AttributeName': 'title',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'content',
#             'AttributeType': 'S'
#         }
#     ]
#
#     key_schema = [
#         {
#             'AttributeName': 'title',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'content',
#             'KeyType': 'RANGE'
#         }
#     ]
#
#     initial_iops = {
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
#
#     dynamodb_table_response = get_dynamodb_client().create_table(
#         AttributeDefinitions=attribute_definitions,
#         TableName=table_name,
#         KeySchema=key_schema,
#         ProvisionedThroughput=initial_iops
#     )
#
#     print("Created DynamoDB table:" + str(dynamodb_table_response))
#
#
# def put_item_on_table():
#     try:
#         response = get_dynamodb_resource().Table("posts").put_item(
#             Item={
#                 'title': "My Gas Chromatograph stopped working!",
#                 'content': "It's been working all year and now my test results are off by 60%",
#                 'date': "10/10/17"
#             }
#         )
#
#         print("A New Post added to the collection successfully!")
#         print(str(response))
#     except Exception as error:
#         print(error)
#
# def put_another_item_on_table():
#     try:
#         response = get_dynamodb_resource().Table("posts").put_item(
#             Item={
#                 'title': "Whatever",
#                 'content': "Whatever",
#                 'info': "some random stuff"
#             }
#         )
#
#         print("A New Post added to the collection successfully!")
#         print(str(response))
#     except Exception as error:
#         print(error)
#
# def update_item_on_table():
#     response = get_dynamodb_resource().Table("posts").update_item(
#         Key={
#               'title': "Whatever",
#               'content': "Whatever"
#         },
#         UpdateExpression="set info = :i",
#         ExpressionAttributeValues={
#             ':i': "lets change the info"
#         },
#         ReturnValues="UPDATED_NEW"
#     )
#
#     print("Updating existing post was success!")
#     print(str(response))
#
# def get_item_on_table():
#     try:
#         response = get_dynamodb_resource().Table("posts").get_item(
#             Key={
#                 'title': "Whatever",
#                 'content': "Whatever"
#             }
#         )
#     except ClientError as error:
#         print(error.response['Error']['Message'])
#     else:
#         item = response['Item']
#         print("Got the item successfully!")
#         print(str(response))
#
#
# def delete_item_on_table():
#     try:
#         response = get_dynamodb_resource().Table("posts").delete_item(
#             Key={
#                 'title': "My Gas Chromatograph stopped working!",
#                 'content': "It's been working all year and now my test results are off by 60%",
#             }
#         )
#     except ClientError as error:
#         if error.response['Error']['Code'] == "ConditionalCheckFailedException":
#             print(error.response['Error']['Message'])
#         else:
#             raise
#     else:
#         print("Deleted item successfully!")
#         print(str(response))
#
#
# def insert_sample_data():
#     table = get_dynamodb_resource().Table("posts")
#
#     with open("postdata.json") as json_file:
#         posts = json.load(json_file, parse_float=decimal.Decimal)
#         for post in posts:
#             title = post['title']
#             content = post['content']
#
#             print("Adding post:", title, content)
#
#             table.put_item(
#                 Item={
#                     'title': title,
#                     'content': content,
#                 }
#             )
#
#     print("Sample post data inserted successfully!")
#
#
# def query_movies_released_in_1985():
#     response = get_dynamodb_resource().Table("Movies").query(
#         KeyConditionExpression=Key('year').eq(1985)
#     )
#
#     for movie in response['Items']:
#         print(movie['year'], ":", movie['title'])
#
#
#
#
# if __name__ == '__main__':
    #create_table()
    #put_item_on_table()
    #put_another_item_on_table()
    #update_item_on_table()
    #get_item_on_table()
    #delete_item_on_table()
    #insert_sample_data()
