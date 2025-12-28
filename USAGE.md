## **📘 OJ 코딩 스터디 GitHub 사용 설명서 (웹 UI 전용)**

이 저장소는 백준 / 프로그래머스 OJ 문제 풀이 스터디를 위해 만들어졌습니다.
모든 작업은 GitHub 웹 페이지에서만 진행하며,
터미널(bash), 로컬 git 명령어는 사용하지 않습니다.

## **1️⃣ 이 레포의 전체 작동 흐름**  

**한 줄 요약**

문제 선택 → Issue 생성 → 브랜치 생성 → 코드 업로드 → PR 생성 → 리뷰 → 머지

**핵심 규칙 요약**

- ❗ 문제를 풀기 전에 반드시 Problem Issue부터 생성
- ❗ 코드는 /problems 폴더 안에서만 업로드 가능
- ❗ 각자는 자기 GitHub ID 이름의 폴더만 수정 가능
- ❗ PR이 머지되면 자동으로:
- 문제 Issue에 커밋 내역 댓글 기록
- Weekly Issue에 체크 표시 + 달성률 자동 반영
- 사용 언어에 따라 언어 라벨 자동 부착

## **2️⃣ Step 1. 문제 Issue 생성하기 (필수)**  

**언제?**

“이 문제를 풀겠다”고 결정했을 때 가장 먼저

**방법**

1. 저장소 상단 메뉴에서 Issues 클릭
2. New issue 버튼 클릭
3. 템플릿 중 Problem 선택
4. 아래 항목 작성

**작성 예시**

- **Platform**: BOJ
- **Problem ID**: 1000
- **Directory**: boj-1000
- Progress 체크박스는 진행하면서 체크
- **Submit new issue** 클릭

📌 이 Issue 번호는 **PR 생성 시 반드시 연결**해야 합니다.

## **3️⃣ Step 2. Weekly Issue 확인 (선택)**

주간 목표 달성률을 자동으로 관리하고 싶을 경우 사용합니다.

**확인 방법**

- Issues 목록에서 [WEEKLY] YYYY-WW 형식의 Issue 확인
- 없다면 운영자가 생성

**작성 방법**

- Weekly Issue 본문에 본인 이름 섹션 + 체크박스 추가

**예시**
### yoon-somang
- [ ] boj-1000
- [ ] pg-42576


⚠️ 체크박스의 문제 이름은** 문제 폴더명과 정확히 동일**해야 자동 체크됩니다.

## **4️⃣ Step 3. 브랜치 생성하기 (웹에서 가능)**  

**왜 브랜치를 사용하나요?**
- main(master)에 직접 업로드 ❌
- PR(Pull Request)을 통한 검토를 위해 필요

**방법**

1. 저장소 상단 Code 탭 클릭
2. 좌측 브랜치 드롭다운 클릭
3. Find or create a branch 입력창에 새 브랜치 이름 입력
예시:
```md
boj-1000-yoon
```
4. Create branch 클릭

➡️ 이제 이 브랜치에서 작업합니다.

## **5️⃣ Step 4. 문제 폴더 및 코드 업로드**  

**반드시 지켜야 하는 폴더 구조**  
```md
problems/
 └─ boj-1000/
     └─ yoon-somang/
         ├─ solution.cpp
         └─ README.md   (선택)
```

**폴더 규칙 요약**

- 문제 폴더 이름은 boj-숫자 또는 pg-숫자 형식만 허용
- 본인 GitHub ID 폴더만 수정 가능
- /problems 외부 수정 시 PR 자동 실패 ❌

**파일 업로드 방법 (GitHub 웹)**

1. problems 폴더로 이동
2. **Add file → Create new file**
3. 경로를 직접 입력
```md
problems/boj-1000/yoon-somang/solution.cpp
```
4. 코드 작성
5. 하단 **Commit changes**
- 메시지 예: Solve boj-1000
- Branch가 본인 브랜치인지 확인
6. Commit changes 클릭

## **6️⃣ Step 5. Pull Request(PR) 생성**  

**PR이란?**
“내 작업을 main(master)에 합쳐주세요”라는 요청입니다.

**생성 방법**
1. 커밋 후 상단의 Compare & pull request 클릭
   (또는 Pull requests → New pull request)
2. base: main, compare: 본인 브랜치 확인
3. PR 본문 작성

**PR 본문 작성 예시 (중요)**  
```md
## Problem
- Platform: BOJ
- Problem ID: boj-1000
- Issue: Closes #12

## Weekly (optional)
Weekly: #34
```
- Closes #문제이슈번호 → 필수
- Weekly: #주간이슈번호 → 자동 체크를 원할 때만 작성
4. **Create pull request** 클릭

## **7️⃣ Step 6. PR 자동 검사 (자동 실행)**  
PR 생성 시 아래 항목들이 자동으로 검사됩니다.
- /problems 외부 파일 수정 여부
- 문제 폴더 이름 규칙 준수 여부
- 본인 GitHub ID 폴더인지 여부
- 코드 확장자 기반 **언어 라벨 자동 부착**

❌ 하나라도 위반 시 PR은 **실패 상태**가 됩니다.

## **8️⃣ Step 7. PR 리뷰 및 머지**
**리뷰**
- 운영자 또는 리뷰어가 코드 확인
- 필요 시 수정 요청

**머지**
- 모든 체크 통과 후
- Merge pull request 버튼 클릭

## **9️⃣ 머지 후 자동으로 처리되는 것들 ✨**
**✅ 문제 Issue 자동 기록**
- PR에 포함된 커밋 목록이 Issue에 자동 댓글

**✅ Weekly Issue 자동 체크**
- 해당 문제 체크박스 자동 [x] 처리
- 전체 달성률 자동 계산 후 댓글

**✅ 언어 라벨 자동 부착**
- 예: lang:Python, lang:C++, lang:Java

## **🔁 자주 발생하는 실수**

- ❌ Problem Issue 없이 PR 생성
- ❌ 폴더 이름 규칙 위반 (boj1000, boj_1000)
- ❌ 다른 사람 폴더 수정
- ❌ PR 본문에 Closes #번호 누락
- ❌ Weekly 체크박스 이름과 문제 폴더명 불일치
