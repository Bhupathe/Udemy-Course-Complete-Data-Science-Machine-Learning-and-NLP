## Building URL Dynamically
## Variable Rule
## Jinja-2 Template Engine

### Jinja2 Template Engine
'''

{{ }} - expressions to print output in html
{% %} - conditions, for loops
{# #} - this is for comments

'''

from flask import Flask, render_template, request, redirect, url_for

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


## This route will run when you submit the form in the route form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username'] ## name, because in html input tag, name is name
        return f'Hello, {name}'
    return render_template('form.html')

## Variable Rule <dtype:variable>
@app.route('/success/<int:score>') # <score> is a parameter # limiting the type of parameter <int: score>
def success(score):
    #return "The Marks you got is, "+ score
    #return f"The Marks you got is, {score}"
    res = ""
    if score >= 50:
        res='PASSED'
    else:
        res='FAILED'

    return render_template('result.html', results=res)

@app.route('/success_for/<int:score>') # <score> is a parameter # limiting the type of parameter <int: score>
def success_for(score):
    #return "The Marks you got is, "+ score
    #return f"The Marks you got is, {score}"
    res = ""
    if score >= 50:
        res='PASSED'
    else:
        res='FAILED'

    exp = {'score': score, 'res': res}
    
    return render_template('result1.html', results=exp)

@app.route('/success_if/<int:score>') 
def success_if(score):
    return render_template('result2.html', results=score)

@app.route('/fail/<int:score>') 
def fail(score):
    return render_template('result1.html', results=exp)

@app.route('/getresults', methods=['POST', "GET"])
def get_result():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        
        total_score = (math + science + data_science + c) / 4
    
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('success_for', score = total_score))

if __name__ == "__main__":
    app.run(debug=True) ## debug parameter will auto-reload whenever there is changes in the file