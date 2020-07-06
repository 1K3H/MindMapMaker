from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mindmapmaker


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/push')
def push():
    receive_test_input = request.form['give_test_input']
    db.inputdata.insert_one({
        'input':receive_test_input
    })
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)