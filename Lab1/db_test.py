from pymongo import MongoClient

#1. Connect to database
client = MongoClient('mongodb://admin:adminpassword@ds127436.mlab.com:27436/dbtest')
#2. Get default database
db = client.get_default_database()
#3. Get collection
blog = db ['blog']

# #4. Insert document
new_post = {
    'title': "Hom nay troi mua",
    'content': 'Toi o nha code'
}

blog.insert_one(new_post)

posts = blog.find() #GET ALL posts in blog
for post in posts:
    print(post)
