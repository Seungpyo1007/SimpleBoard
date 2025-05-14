# 🚀 EC2 + PostgreSQL + Flask 배포 가이드

## 1. EC2 서버 준비
1. AWS EC2 인스턴스 생성 (Ubuntu 22.04 추천)
2. 보안 그룹 인바운드 규칙 설정
    - SSH: 22 포트 (내 IP)
    - HTTP: 80 포트 (모두 허용)
    - Flask용: 5000 포트 (테스트용, 필요시 5001 포트로 변경)
    - PostgreSQL: 5432 포트 (내 IP 또는 내부망)

3. SSH 접속
```bash
ssh -i <key.pem> ubuntu@<EC2 퍼블릭 IP>
```

## 2. 필수 패키지 설치
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv git postgresql postgresql-contrib
```

## 3. PostgreSQL 설정
### 3-1. PostgreSQL 초기 설정
```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE your_db_name;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_username;
```
```bash
\q
```

### 3-2. 외부 접속 허용
```bash
sudo nano /etc/postgresql/14/main/postgresql.conf
```
- `listen_addresses = '*'` 로 변경

```bash
sudo nano /etc/postgresql/14/main/pg_hba.conf
```
- 맨 아래 추가:
```
host    all             all             0.0.0.0/0               md5
```

### 3-3. PostgreSQL 재시작
```bash
sudo systemctl restart postgresql
```

## 4. Flask 애플리케이션 배포
### 4-1. 애플리케이션 코드 준비
```bash
git clone <YOUR_REPO_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 4-2. 가상환경 및 패키지 설치
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4-3. Flask 실행 (테스트용)
```bash
python app.py
```
- 브라우저에서 `http://<EC2 IP>:5000/` 접속 → "Flask + PostgreSQL 서버 작동 중!" 확인

## 5. 배포 환경 구성 (Gunicorn + Nginx)
### 5-1. Gunicorn 설치 및 실행
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 5-2. Nginx 설치 및 설정
```bash
sudo apt install -y nginx
sudo nano /etc/nginx/sites-available/flask_app
```
#### flask_app 설정 예시
```nginx
server {
    listen 80;
    server_name <EC2 퍼블릭 IP>;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## 6. 프로세스 관리 (Supervisor 예시)
```bash
sudo apt install -y supervisor
sudo nano /etc/supervisor/conf.d/flask_app.conf
```
#### flask_app.conf 설정 예시
```ini
[program:flask_app]
directory=/home/ubuntu/<YOUR_PROJECT_FOLDER>
command=/home/ubuntu/<YOUR_PROJECT_FOLDER>/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
autostart=true
autorestart=true
stderr_logfile=/var/log/flask_app.err.log
stdout_logfile=/var/log/flask_app.out.log
user=ubuntu
```

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start flask_app
```

## 7. 방화벽 및 보안 (필수)
- AWS 보안그룹에서 5000 포트는 테스트 후 닫기
- nginx 80 포트만 외부 노출
- 필요시 SSL 인증서 (Let's Encrypt) 적용

## 8. 최종 확인
- 웹 브라우저에서 `http://<EC2 퍼블릭 IP>/users` 접속
- PostgreSQL 연결 성공 및 API 정상 응답 확인
