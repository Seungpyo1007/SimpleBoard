# 📄 API 명세서 — Flask + PostgreSQL

## 📌 Base URL
```
http://<서버 IP>:5000/ # 저같은 경우는 5001포트로 하였습니다. (5000포트 이미 사용)
```

---

## 🏠 GET `/`
서버가 정상 작동 중인지 확인하는 헬스 체크용 API입니다.

### ✅ Response (200 OK)
```text
Flask + PostgreSQL 서버 작동 중!
```

# 👥 GET /users

## PostgreSQL의 users 테이블에서 모든 사용자 목록을 조회합니다.

### ✅ Request

    Method: GET

    URL: /users

### ✅ Response (200 OK)
```agsl
[
  {
    "id": 1,
    "name": "홍길동",
    "email": "hong@example.com"
  },
  {
    "id": 2,
    "name": "김철수",
    "email": "kim@example.com"
  }
]

```

# ➕ POST /users

## 새로운 사용자를 users 테이블에 추가합니다.
### ✅ Request

    Method: POST

    URL: /users

    Content-Type: application/json

    Body:

```
{
"name": "이영희",
"email": "lee@example.com"
}
```

### ✅ Response (201 Created)

```
{
  "status": "사용자 추가됨"
}
```

# 🗄 users 테이블 스키마 (참고용)

```agsl
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

# 🧪 Example CURL 명령어

## 🔍 사용자 목록 조회

```agsl
curl -X GET http://<서버 IP>:5000/users
```

## ➕ 사용자 추가

```agsl
curl -X POST http://<서버 IP>:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "이영희", "email": "lee@example.com"}'
```

---