from flask import Flask, request, jsonify
app = Flask('__nira__')
@app.route('/')
def hello_world():
    return 'Hello, Library Management System!'
if ('__nira__') == '__main__':
    app.run(debug=True)