from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello')
def index():
    name = request.args.get('name', 'Nobody')
    if name:
        greeting = f"Hello, {name}"
    else:
        greeting = f"Hello World!"

    return render_template("index.html", greeting=greeting)

@app.route('/form', methods=['POST', 'GET'])
def form():
    greeting = "Hello World"
    if(request.method == 'POST'):
        name = request.form['name']
        greet = "Hello " + request.form['greet']
        greeting = f"{greet}, {name}" 
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":
    app.run()