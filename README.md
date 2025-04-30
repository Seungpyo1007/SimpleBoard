# 📝 SimpleBoard - React Native Bulletin Board App

**SimpleBoard**는 React Native와 Expo를 기반으로 개발된 심플하고 직관적인 **모바일 게시판 앱**입니다. 사용자들은 글을 작성하고, 게시글 목록을 열람하며, 각 게시글의 상세 내용을 확인할 수 있습니다. 이 앱은 게시판 기능의 핵심을 간결하게 담아, 모바일 UI/UX를 고려한 최소한의 기능으로 구성되어 있습니다.

<br>

## 🚀 주요 기능

- 📄 게시글 목록 보기 (최신순 정렬)
- 🖊️ 게시글 작성 기능 (제목, 내용 입력)
- 🔍 게시글 상세 조회
- 🧹 게시글 삭제 기능
- 💾 로컬 상태 저장 (비휘발성 DB 연동 전의 간이 스토리지 구조)

<br>

## 🛠️ 사용 기술 스택

| 기술 | 설명 |
|------|------|
| **React Native** | 크로스 플랫폼 앱 개발 프레임워크 |
| **Expo** | 빠른 개발과 디버깅을 지원하는 React Native 플랫폼 |
| **React Navigation** | 화면 간 이동 구현을 위한 라우팅 라이브러리 |
| **AsyncStorage (또는 useState)** | 간단한 로컬 데이터 저장 처리 |
| **TypeScript (선택사항)** | 정적 타입을 통한 코드 안정성 향상 |

<br>

## 📁 프로젝트 구조

SimpleBoard/ ├── App.js ├── components/ │ └── PostItem.js ├── screens/ │ ├── HomeScreen.js │ ├── WriteScreen.js │ └── DetailScreen.js ├── navigation/ │ └── StackNavigator.js └── assets/


- `HomeScreen`: 게시글 리스트 화면
- `WriteScreen`: 글쓰기 폼 UI 및 저장 처리
- `DetailScreen`: 게시글 세부 정보 표시
- `PostItem`: 게시글을 리스트에서 개별 렌더링하는 컴포넌트
- `navigation/StackNavigator`: 화면 간 네비게이션 구조 관리

<br>

## ⚙️ 설치 및 실행 방법

```bash
# 1. 프로젝트 클론
git clone https://github.com/your-username/SimpleBoard.git
cd SimpleBoard

# 2. 패키지 설치
npm install

# 3. Expo 개발 서버 실행
npx expo start
