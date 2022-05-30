# Hassan Mahmood 181255

from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def result():
    num_1 = request.form.get("num_1", type=int)
    num_2 = request.form.get("num_2", type=int)
    operation = request.form.get("opr", type=str)
    # operation = request.form.get("operation")
    if(operation == '+'):
        result = num_1 + num_2
    elif(operation == '-'):
        result = num_1 - num_2
    elif(operation == '*'):
        result = num_1 * num_2
    elif(operation == '/'):
        result = num_1 / num_2
    else:
        result = 'Invalid'
    entry = result
    return render_template('home.html',entry=entry, a=num_1, b=num_2,c=operation)

if __name__ == '__main__':
    app.run(debug=True)
