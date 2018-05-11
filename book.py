import os
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient

class Book:

    def __init__(self):
        if "MONGOHOST" in os.environ:
            mongo_host = os.environ['MONGOHOST']
        else:
            mongo_host = 'mongo'
        print("Connecting to mongo: {0}:{1}".format(
            mongo_host,
            "27017"
            ))
        client = MongoClient(mongo_host, 27017)
        self.db = client.books_db
        self.books = self.db.books

    def add_book(self, title, author):
        post_data = {
            'title': title,
            'author': author
        }
        result = self.books.insert_one(post_data)
        return dumps(post_data)

    def del_book(self, id):
        result = self.books.delete_one({'_id': ObjectId(id)})
        print("delete result: {0}".format(result.deleted_count))
        if result.deleted_count == 0:
            return False
        return "{}"

    def get_all_books(self):
        result = ""
        for book in self.books.find():
            print("book: {0}".format(book))
            result += str(book)
        print("result: {0}: ".format(result))
        if len(result) == 0:
            result = "{}"
        return result

    def json_list(self):
        result = self.get_all_books()
        return result
