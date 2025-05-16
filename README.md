# 📝 SimpleBoard - React Native Bulletin Board App

**SimpleBoard**는 React Native와 Expo 기반의 심플한 **목록형 게시판 앱**입니다. 사용자들은 게시글을 작성하고, 목록을 조회하며, 상세 내용을 확인할 수 있습니다.

> 이 프로젝트는 AWS EC2에 PostgreSQL과 Flask 백엔드 서버를 구성하고, 해당 서버와 React Native 앱이 연동되도록 설계되었습니다.

---

## 🚀 주요 기능

* 📄 게시글 목록 보기 (최신순 정렬)
* 🔊 게시글 작성 기능 (제목, 내용 입력)
* 🔍 게시글 상세 조회
* 🧹 게시글 삭제 기능
* 🔗 Flask + PostgreSQL 백엔드 연동 (REST API 사용)

---

## 🛠️ 사용 기술 스택

| 구루     | 기술                                                      |
| ------ | ------------------------------------------------------- |
| 프론트엔드  | React Native, Expo, React Navigation                    |
| 백엔드    | Python, Flask                                           |
| 데이터베이스 | PostgreSQL                                              |
| 인프라    | AWS EC2 (Ubuntu)                                        |
| 상태관리   | useState, AsyncStorage (간이)                             |
| 개발환경   | **Firebase Studio (IDX)**, **IntelliJ IDEA (2024.1.7)** |

---

## 📁 프로젝트 구조

```
SimpleBoard/
🔽️ (React Native Files)
🔽️ backend/ # Flask API 서버
🔽️ database/ # PostgreSQL 스킨링
🔽️ docs/ # 시스템 문서
```

* [`app/`](./app): 홈, 작성, 상세 화면 구성
* [`backend/`](./backend): Flask REST API 서버 코드
* [`database/schema.sql`](./database/schema.sql): PostgreSQL 테이블 구조
* 시스템 문서:

  * 📘 [시스템 아키텍처 설명서](./docs/architecture.md)
  * 📙 [Flask API 명세서](./docs/api_spec.md)
  * 📕 [배포 가이드 (EC2 + PostgreSQL + Flask)](./docs/deployment_guide.md)

---

## 최종 프로젝트 구조

```
SimpleBoard/
├── App.js
├── package.json
├── .gitignore
├── README.md                   # ✅ React Native 앱 기준 메인 설명서

├── components/                # 📦 재사용 가능한 UI 코너트
├── app/                       # 📱 게시판 UI 화면 (Home, Write, Detail)
├── navigation/                # 🤭 화면 전환 설정 (React Navigation)
├── assets/                    # 🖼️ 이미지 및 기타 리소스

├── backend/                   # 🐍 Flask 백엔드 API 서버
│   ├── app.py
│   ├── config.py              # 필요하면 추가 예정
│   ├── models.py              # 필요하면 추가 예정
│   ├── routes.py              # 필요하면 추가 예정
│   ├── requirements.txt       
│   └── .env.example           # 필요하면 추가 예정

├── database/                  # 📓️ PostgreSQL 스킨링 정의
│   └── schema.sql

├── docs/                      # 📚 시스템 아키텍처 및 배포 문서
│   ├── architecture.md        # 전체 시스템 구조 단어그램 및 설명
│   ├── api_spec.md            # Flask API 명세서
│   └── deployment_guide.md    # EC2 + PostgreSQL + Flask 배포 가이드
```

## ⚙️ 설치 및 실행 방법

### 📱 React Native (프론트엔드)

```bash
# 1. 프로젝트 클론톤
$ git clone https://github.com/your-username/SimpleBoard.git
$ cd SimpleBoard

# 2. 패키지 설치
$ npm install

# 3. Expo 개발 서버 실행
$ npx expo start
```

---

## 아키텍처 구성도

```
[React Native 앱] <--> [Flask REST API] <--> [PostgreSQL DB]
                              ▲
                              │
                  IDX (Firebase Studio)
```

**Firebase Studio**는 팀 프로젝트 시 환경 충돌 없이 동일한 조건의 개발 환경을 제공하는 가장 큰 장점입니다.

### 📌 기타

* Firebase Studio는 아직 베타 데이터이며, 건호적인 네트워크 문제 또는 빌드 오류가 발생할 수 있습니다.
* Expo 앱 실행 시 웹 미리보기 또는 QR 스캔 방식이 지원됩니다.
