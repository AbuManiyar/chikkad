from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    operation = request.form['operator']
    num1 = request.form['num1']
    num2 = request.form['num2']
    
    
    if operation == 'add':
        result = int(num1)+int(num2)
    if operation == 'multiply':
        result = int(num1)*int(num2)
    if operation == 'subtract':
        result = int(num1)-int(num2)
    if operation == 'divide':
        result = int(num1)/int(num2)
    
    return render_template("display_calculator.html", result = result)


if __name__ == "__main__":
    app.run(debug = True)