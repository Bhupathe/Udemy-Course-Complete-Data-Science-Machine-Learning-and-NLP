"""Integrate HTML file into web framework"""

from flask import Flask, render_template

## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return """
<html>
    <body>
        <h1> Welcome to the Flask Course </h1>
    </body>
</html>
"""

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def a():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True) ## debug parameter will auto-reload whenever there is changes in the file