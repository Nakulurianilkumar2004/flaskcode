from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

# MongoDB connection
mongo_uri = "mongodb+srv://anilkumar:9392832240@cluster0.guvwb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client['quiz_app']
users_collection = db['users']

@app.route('/api/store-user-details', methods=['POST'])
def store_user_details():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    interest = data.get('interest')

    if not all([name, email, phone, interest]):
        return jsonify({'error': 'All fields are required'}), 400

    try:
        user_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'interest': interest
        }
        users_collection.insert_one(user_data)
        return jsonify({'message': 'User details saved successfully'}), 200
    except Exception as e:
        print(f"Error saving user: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
