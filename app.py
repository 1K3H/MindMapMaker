from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mindmapmaker


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/make', methods=['POST'])
def save_node():
    receive_from_input = request.form['give_from_input']
    receive_to_input = request.form['give_to_input']
    receive_edge_id = request.form['give_edge_id']
    db.nodes.insert_one({
        'from': receive_from_input,
        'to': receive_to_input,
        'edge': receive_edge_id
    })
    return jsonify({'result':'success'})

@app.route('/load', methods=['GET'])
def list_node():
    nodes = list(db.nodes.find({}, {'_id':False}))
    return jsonify({'result':'success', 'nodes':nodes})

@app.route('/delete', methods=['POST'])
def delete_node():
    receive_from_input = request.form['give_from_input']
    receive_to_input = request.form['give_to_input']
    receive_edge_id = request.form['give_edge_id']
    db.nodes.delete_one({
        'from': receive_from_input,
        'to': receive_to_input,
        'edge': receive_edge_id
    })
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)