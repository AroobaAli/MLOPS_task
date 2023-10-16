from flask import Flask, render_template, request
from code_2 import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    input_data = request.form['input_data']
    result = predict(input_data)
    return render_template('index.html', input_data=input_data, result=result)

if __name__ == '__main__':
    app.run(debug=True)
