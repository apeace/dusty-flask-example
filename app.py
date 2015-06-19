import os

from flask import Flask
from pymongo import MongoClient, ReturnDocument

app_name = os.getenv('APP_NAME')
app = Flask(app_name)
mongo = MongoClient(os.getenv('MONGO_HOST', 'localhost'), int(os.getenv('MONGO_PORT', 27017)))
collection = mongo['hello-world']['data']

def _get_and_increment_count_from_mongo(key):
    result = collection.find_one_and_update({'_id': key},
                                            {'$inc': {'seen': 1}},
                                            upsert=True,
                                            return_document=ReturnDocument.AFTER)
    return result['seen']

@app.route('/')
def hello_world():
    my_count = _get_and_increment_count_from_mongo(app_name)
    shared_count = _get_and_increment_count_from_mongo('shared')
    return '''
    <p>Hello world! My name is {}!</p>
    <p>I have been seen <b>{}</b> times.</p>
    <p>My friends and I have been seen a total of <b>{}</b> times.</p>
    '''.format(app_name, my_count, shared_count)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
