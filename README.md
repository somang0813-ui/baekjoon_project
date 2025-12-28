# 🧠 OJ 코딩 스터디 (GitHub Web 기반)

이 저장소는 **백준 / 프로그래머스 OJ 문제 풀이 스터디**를 위한 공간입니다.  
모든 작업은 **GitHub 웹 UI만 사용**하여 진행하며,  
풀이 결과뿐 아니라 **풀이 과정과 진행 상황을 기록·공유**하는 것을 목표로 합니다.

---

## 🚀 이 스터디의 핵심 컨셉

- 문제를 고르고 **Issue로 먼저 선언**
- 풀이 진행을 **Issue + PR + 커밋 로그**로 기록
- 코드는 **각자 폴더에서 독립적으로 관리**
- PR 머지 시:
  - 문제 Issue에 **커밋 내역 자동 기록**
  - Weekly 목표에 **자동 체크 + 달성률 계산**
  - 사용 언어에 따라 **라벨 자동 부착**

👉 **“정답 공유”보다 “과정 기록 + 피드백” 중심 스터디**

---

## 🧩 전체 사용 흐름 (요약)

문제 선택  
↓  
Problem Issue 생성  
↓  
브랜치 생성 (웹)  
↓  
코드 업로드 (/problems)  
↓  
Pull Request 생성  
↓  
리뷰 & 머지  
↓  
자동 기록 & Weekly 체크  

---

## 📂 디렉터리 구조 규칙  
'''nd
problems/
└─ boj-1000/ ← 문제 폴더 (boj-숫자 / pg-숫자)
└─ yoon-somang/ ← 본인 GitHub ID
├─ solution.cpp
└─ README.md ← (선택) 풀이 설명  

### 규칙 요약
- `/problems` 폴더 **외부 수정 불가**
- 문제 폴더 이름은 `boj-숫자` 또는 `pg-숫자`만 허용
- **자기 GitHub ID 폴더만 수정 가능**
- 위반 시 PR은 자동 실패 ❌

---

## 📝 Issue & PR 규칙

### ✅ Problem Issue (필수)
- 문제를 풀기 전에 반드시 생성
- PR에서 아래 형식으로 연결
```md
Closes #문제이슈번호

### 📅 Weekly Issue (선택)  

- 주간 목표를 체크박스로 관리

- PR 본문에 아래를 작성하면 자동화 활성화

- Weekly: #Weekly이슈번호

###🤖 자동화로 되는 것들

- PR 경로/규칙 자동 검사

- 문제 폴더 이름 규칙 강제

- PR에 언어 라벨 자동 부착

-- 예: lang:Python, lang:C++

- PR 머지 시:

- 문제 Issue에 커밋 목록 자동 댓글

- Weekly Issue에 체크 표시 자동 반영

- Weekly 달성률 자동 계산

###📘 자세한 문서

📖 USAGE.md : 처음 사용하는 사람을 위한 상세 사용법

🤝 CONTRIBUTING.md : 규칙 요약

❓ FAQ.md : PR 실패/자동화 관련 질문

🛠 MAINTAINER_GUIDE.md : 운영자용 가이드
