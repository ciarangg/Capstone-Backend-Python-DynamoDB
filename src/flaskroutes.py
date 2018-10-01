from flask import Flask

from flask import jsonify
from flask import request


from flask_dynamo import Dynamo


app = Flask(__name__)

dynamo = Dynamo(app)

@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/post')
def create_user():
    dynamo.tables['post'].put_item(TableName={'post'})

# app.config['DYNAMO_TABLES'] = [
#     {
#          TableName='user',
#          KeySchema=[dict(AttributeName='username', KeyType='HASH')],
#          AttributeDefinitions=[dict(AttributeName='username', AttributeType='S')],
#          ProvisionedThroughput=dict(ReadCapacityUnits=10, WriteCapacityUnits=10)
#     }, {
#          TableName='post',
#          KeySchema=[dict(AttributeName='name', KeyType='HASH')],
#          AttributeDefinitions=[dict(AttributeName='name', AttributeType='S')],
#          ProvisionedThroughput=dict(ReadCapacityUnits=10, WriteCapacityUnits=10)
#     }
# ]


# @app.route('/')
# def hello_world():
#     return 'Hello'

# @app.route('/post')
# def post_route():
#     return 'Hello, POSTTT!'

# @app.route('/comment')
# def comment_route():
#     return 'Hello, COMMENT!'
#
# @app.route('/user')
# def user_route():
#     return 'Hello, USER!'






# postdata = [
#   {
#     "title": "My GC Machine isn't working",
#     "content": "It's been working all year and last month my sample results are off by 70%"
#   },
#   {
#     "title": "My PCRs aren't working",
#     "content": "I'm using a gradient PCR and I've tried 60, 70, 75, and 80 degrees celcius for the annealing process what am i doing wrong!"
#   },
#   {
#     "title": "My RNA keeps degrading :(",
#     "content": "RNA is literally the worst. plz give me moral support"
#   },
#   {
#     "title": "I accidentally created a Blackhole",
#     "content": "I made a blackhole in my lab and now it's eating everything up. How do I stop it?"
#   }
# ]
#
#
# @app.route('/', methods=['GET'])
# def hello_world():
#     return jsonify({'message' : 'Hello, World!'})
#
# @app.route('/post', methods=['GET'])
# def returnAll():
#     return jsonify({'posts': postdata})
#
# @app.route('/post/<string:title>', methods=['GET'])
# def returnOne(title):
#     theOne = postdata[0]
#     for i,q in enumerate(postdata):
#       if q['title'] == title:
#         theOne = postdata[i]
#     return jsonify({'posts' : theOne})
#
# @app.route('/quarks', methods=['POST'])
# def addOne():
#     new_post = request.get_json()
#     postdata.append(new_post)
#     return jsonify({'posts' : postdata})
#
# @app.route('/quarks/<string:name>', methods=['PUT'])
# def editOne(title):
#     new_post = request.get_json()
#     for i,q in enumerate(postdata):
#       if q['title'] == title:
#           postdata[i] = new_post
#     qs = request.get_json()
#     return jsonify({'posts' : postdata})
#
# @app.route('/quarks/<string:name>', methods=['DELETE'])
# def deleteOne(title):
#     for i,q in enumerate(postdata):
#       if q['title'] == title:
#         del postdata[i]
#     return jsonify({'posts' : postdata})
#
# if __name__ == "__main__":
#     app.run(debug=True)


