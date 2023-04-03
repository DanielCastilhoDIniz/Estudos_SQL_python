import pymongo as pyM
import datetime

client = pyM.MongoClient("mongodb://localhost:27017")

db = client.test
collection = db.test_colletcion


post = {
    "autor": "Daniel",
    "text": "MongoDb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}


# criando uma collection
posts = db.post

post_id = posts.insert_one(post).inserted_id

print(db.list_collection_names())
print(posts.find_one())

new_posts = [
    {
        "autor": "Daniel",
        "text": "Another post",
        "tags": ["bulks", "post", "insert"],
        "date": datetime.datetime.utcnow()
    },
    {
        "autor": "Dev",
        "text": "maybe someday",
        "title": "Mongo is fun",
        "date": datetime.datetime.utcnow()
    }
]

result = posts.insert_many(new_posts)

print(result.inserted_ids)



for post in posts.find():
    print(post)