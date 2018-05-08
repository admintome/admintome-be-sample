import tornado.web
import book
import json
 
 
class DelHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
 
    def get(self):
        id = self.get_argument('id')
        result = self.books.del_book(id)
        if result:
            self.write("Deleted book: {0} succsessfully".format(id))
            self.set_status(200)
        else:
            self.write("Book '{0}' not found".format(id))
            self.set_status(404)
