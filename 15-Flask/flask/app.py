from flask import Flask

'''
It creates an instance of the Flask class, 
which will be your WSGI (Web Server Gateway INterface) application.
'''

## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to this beautiful Flask course. This will be amazing course."

@app.route('/index')
def index():
    return "This is index page."

if __name__ == "__main__":
    app.run(debug=True) ## debug parameter will auto-reload whenever there is changes in the file