from flask import Blueprint, request, jsonify
from .models import db, User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def health_check():
    return "Flask + PostgreSQL 서버 작동 중!", 200

@main_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        if not data or not 'name' in data or not 'email' in data:
            return jsonify({'error': 'Missing name or email in request body'}), 400

        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        # The API spec asks for {"status": "사용자 추가됨"} and 201 Created
        # While typically one might return the created resource, we'll follow the spec.
        return jsonify({"status": "사용자 추가됨"}), 201
    except Exception as e:
        db.session.rollback()
        # Check for unique constraint violation for email
        if 'unique constraint' in str(e).lower() and 'users_email_key' in str(e).lower():
            return jsonify({'error': f"User with email {data.get('email')} already exists."}), 409
        return jsonify({'error': str(e)}), 500
