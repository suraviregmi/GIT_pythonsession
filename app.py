# -*- coding: utf-8 -*-
"""
Simple flask based applicion
"""
# import Flask class from flask module
from flask import Flask

# app is instance of flask class
print (__name__)
app = Flask(__name__)


# makes this function root path of our application
@app.route('/')
def index():
    """
    index page  of our web app
    """
    return "this is main page"

@app.route('/hello/<name>')
@app.route('/hello')

def hello(name):
    """
    hellos back to user
    """
    return"hello {} !".format(name)
@app.route('/hello/<int:user_id>')
def user_details(user_id):
    """
    return user detail for given user
    """
    return"{FullName} {Age} {Location}".format(**{
    'FullName': 'john Doe',
    'Age': 'Unknown',
    'Location': 'Kathmandu'
        })

if __name__ == '__main__':
  # only when __name__ is __main__win   
    app.run(debug=True)
