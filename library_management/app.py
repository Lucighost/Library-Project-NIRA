from flask import Flask, request, jsonify
app = Flask('__nira__')
@app.route('/')
def hello_world():
    return 'Hello, Library Management System!'
if ('__nira__') == '__main__':
    app.run(debug=True)

    books = []
class Book:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author, "year": self.year}
