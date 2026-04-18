from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__) 

# Dummy database to demonstrate functionality
users_db = {}  

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users_db:
        return jsonify({'message': 'User already exists!'}), 409
    
    hashed_password = generate_password_hash(password)
    users_db[username] = hashed_password
    return jsonify({'message': 'User registered successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username not in users_db or not check_password_hash(users_db[username], password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    return jsonify({'message': 'Login successful!'}), 200

@auth_bp.route('/validate_token', methods=['POST'])
def validate_token():
    token = request.headers.get('Authorization')
    if token == 'Bearer dummy_token': 
        return jsonify({'message': 'Token is valid!'}), 200
    return jsonify({'message': 'Invalid token!'}), 401
