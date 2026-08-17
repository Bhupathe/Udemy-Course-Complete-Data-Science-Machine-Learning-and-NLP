"""Use of HTML Verbs: GET and POST"""

from flask import Flask, render_template, request

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

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def a():
    return render_template('about.html')

## Post HTTP Verb
@app.route('/form', methods=['GET', 'POST'])
def f():
    if request.method == 'POST':
        name = request.form['name'] ## name, because in html input tag, id is name
        #print(f"Hello, {name}")
        return f'Hello, {name}'
    return render_template('form.html')

## This route will run when you submit the form in the route form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username'] ## name, because in html input tag, name is name
        return f'Hello, {name}'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True) ## debug parameter will auto-reload whenever there is changes in the file