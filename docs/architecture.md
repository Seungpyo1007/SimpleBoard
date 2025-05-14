# 🏗️ 시스템 아키텍처 설명서

## 📦 전체 시스템 개요

본 프로젝트는 **모바일 게시판 앱(SimpleBoard)**으로, 프론트엔드는 React Native + Expo로 구성되고, 백엔드는 Flask REST API + PostgreSQL로 구성됩니다.

- 모바일 앱은 게시글 작성, 조회, 삭제 등의 기능을 제공하며, REST API를 통해 백엔드 서버와 통신합니다.
- 백엔드 서버는 AWS EC2에 배포되며, PostgreSQL과 연동하여 데이터를 저장/조회합니다.
- 클라우드 개발 환경으로는 **Firebase Studio (IDX)**를 사용하여, 언제 어디서나 동일한 개발 환경을 유지할 수 있도록 설정했습니다.

---

## 🔧 개발 환경 구성 - Firebase Studio (IDX)

### ✅ Firebase Studio (IDX) 도입 배경

- 로컬 개발 환경 세팅 없이 **바로 브라우저에서 개발 가능**
- 팀원 간 개발 환경 차이 없이 **동일한 컨테이너 기반 개발 환경 공유**
- React Native + Python + PostgreSQL 개발에 필요한 기본 도구가 미리 세팅되어 있어 빠른 시작 가능

### 📂 IDX 환경 구조

IDX 내에서는 아래와 같은 구조로 프로젝트를 관리하였습니다:

```
/workspace/
├── / # React Native App
├── backend/ # Flask API 서버
├── database/ # PostgreSQL 스키마
└── docs/ # 문서
```
### ⚙️ IDX 세팅 방법

1. **Firebase Studio 접속**  
   https://firebase.google.com/studio 또는 https://idx.dev 접속

2. **GitHub 연동 및 리포지토리 선택**
    - 로그인 후 `Start from GitHub` 선택
    - `SimpleBoard` 저장소 연결

3. **환경 선택**
    - 템플릿은 `React Native` 또는 `Custom Dockerfile` 기반으로 선택
    - 필요 시 `Dockerfile` 또는 `.devcontainer/devcontainer.json` 추가로 세팅

4. **환경 초기화**
   ```bash
   # 프론트엔드
   cd SimpleBoard
   npm install
   npx expo start

   # 백엔드
   cd backend
   pip install -r requirements.txt
   flask run

### 🧩 아키텍처 구성도

```
[React Native 앱] <--> [Flask REST API] <--> [PostgreSQL DB]
▲
│
IDX (Firebase Studio) - 브라우저 기반 통합 개발 환경
# Firebase Studio는 팀 프로젝트 시 로컬 환경 충돌 없이 동일한 조건의 개발 환경 제공이 가장 큰 장점입니다.
```
