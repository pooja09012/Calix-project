# app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb-service:27017/")  # Use the Kubernetes Service name

db = client["mydatabase"]
collection = db["records"]

@app.route('/api/records', methods=['GET'])
def get_records():
    records = list(collection.find())
    return jsonify(records), 200

@app.route('/api/record/<id>', methods=['GET'])
def get_record(id):
    record = collection.find_one({"_id": id})
    if record:
        return jsonify(record), 200
    else:
        return jsonify({"message": "Record not found"}), 404

@app.route('/api/record', methods=['POST'])
def add_record():
    data = request.json
    inserted = collection.insert_one(data)
    return jsonify({"message": "Record added", "id": str(inserted.inserted_id)}), 201

@app.route('/api/record/<id>', methods=['PUT'])
def update_record(id):
    data = request.json
    updated = collection.update_one({"_id": id}, {"$set": data})
    if updated.matched_count > 0:
        return jsonify({"message": "Record updated"}), 200
    else:
        return jsonify({"message": "Record not found"}), 404

@app.route('/api/record/<id>', methods=['DELETE'])
def delete_record(id):
    deleted = collection.delete_one({"_id": id})
    if deleted.deleted_count > 0:
        return jsonify({"message": "Record deleted"}), 200
    else:
        return jsonify({"message": "Record not found"}), 404

# MongoDB connection URL
client = MongoClient("mongodb://mongodb:27017/")  # Use the Kubernetes Service name


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


