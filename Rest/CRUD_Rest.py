from flask import Flask, json, request, Response
from DB.DB_Controller import *

app = Flask(__name__)


@app.route("/api/", methods=['GET'])
def index():
    print("Another **GET** Request Found")
    return Response(json.dumps(DBController.get_all()), mimetype='application/json')


@app.route("/api/data/<int:num>", methods=['GET'])
def get_document(num):
    print(num)
    data = DBController.get_by_id(num)
    print(data)
    return Response(json.dumps(data), mimetype='application/json')


@app.route("/api/del/<int:num>", methods=['DELETE'])
def delete_document(num):
    status = DBController.delete_by_id(num)
    print(status)
    if status:
        return Response(json.dumps({"Status": "Deleted"}), mimetype='application/json')
    else:
        return Response(json.dumps({"Status": "Error"}), mimetype='application/json')


@app.route('/api/save', methods=['POST'])
def save_document():
    req_data = request.get_json()
    doc_name = req_data['doc_name']
    author = req_data['author']
    descrip = req_data['description']
    status = DBController.add(doc_name, author, descrip)
    if status:
        return Response(json.dumps({"Status": "Success"}), mimetype='application/json'), 200
    else:
        return Response(json.dumps({"Status": "Error"}), mimetype='application/json')


@app.route('/api/update/<int:num>', methods=['PUT'])
def update_document(num):
    req_data = request.get_json()
    doc_name = req_data['doc_name']
    author = req_data['author']
    description = req_data['description']
    if DBController.update_by_id(num, doc_name, author, description):
        return Response(json.dumps({"Status": "Success"}), mimetype='application/json'), 200
    else:
        return Response(json.dumps({"Status": "Error"}), mimetype='application/json'), 404


if __name__ == '__main__':
    app.run(host='localhost', port=1999, debug=True)


