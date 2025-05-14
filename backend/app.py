from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# PostgreSQL 연결 함수
def get_db_connection():
    return psycopg2.connect(
        host='00.000.00.00',        # AWS EC2의 PostgreSQL IP
        database='your_db_name',    # 사용할 DB 이름
        user='your_username',       # DB 사용자 이름
        password='your_password',   # 비밀번호
        port=5432                   # 기본 포트
    )

@app.route('/')
def home():
    return 'Flask + PostgreSQL 서버 작동 중!'

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('SELECT * FROM users;')  # users 테이블
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    users = [dict(row) for row in rows]
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (name, email) VALUES (%s, %s)',
        (name, email)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'status': '사용자 추가됨'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
