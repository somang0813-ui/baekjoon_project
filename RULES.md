# RULES (OJ Study Repository)

이 레포는 "문제별 + 사람별"로 파일을 분리해 충돌을 최소화합니다.

## 1) 폴더/파일 생성 규칙 (가장 중요)

### (1) 문제 폴더 생성
- 위치: `problems/`
- 형식:
  - 백준: `BOJ_<번호>`  예) `BOJ_1000`
  - 프로그래머스: `PGS_<문제명>` 예) `PGS_무인도여행`
  - 리트코드: `LC_<번호 or slug>` 예) `LC_1_TwoSum`

### (2) 문제 폴더 내부 구조
각 문제 폴더에는 다음을 둡니다.

- `README.md` : 문제 링크/태그/주의사항 (짧게)
- `<name>/` : 사람별 폴더 (각자 1개)

예시:  
- problems/BOJ_1000/  
README.md  
yoon/  
solution.py  
friendA/  
main.cpp
  
### (3) 사람별 폴더 규칙
- 사람 폴더명은 가능한 한 고정 (예: github id, 영어 닉네임)
- 예: `yoon`, `minsu`, `hana`

### (4) 코드 파일명 규칙 (통일)
- Python: `solution.py`
- C++: `main.cpp`
- Java: `Main.java`
- (추가 언어가 필요하면 팀에서 합의 후 확장)

### (5) 금지 사항
- 다른 사람 폴더의 코드를 직접 수정하지 않는다.
- 루트에 무작정 코드 파일을 만들지 않는다. (항상 `problems/` 아래)

## 2) 커밋 메시지 규칙 (권장)
형식 예시:
- `boj 1000: implement basic I/O`
- `pgs 무인도여행: bfs solution`
- `chore: update rules`

## 3) PR/브랜치 규칙 (선택)
### A) 간단 모드 (직푸시)
- main에 바로 push 가능
- 단, 반드시 "본인 폴더"만 수정

### B) PR 모드 (권장)
- 브랜치명: `feature/<site>-<problem>-<name>`
  - 예: `feature/boj-1000-yoon`
- PR 올릴 때:
  - 변경한 문제 폴더 링크를 설명에 적기
  - 가능하면 간단한 풀이 요약 2~3줄

## 4) 문서 규칙
- 스터디 기록은 `weekly/`에 남긴다.
- 템플릿은 `templates/`에만 둔다.
