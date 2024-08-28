# Django_team_project
# 장발장터
장발장터는 사용자들이 제품을 게시하고, 검색하며, 좋아요를 누를 수 있는 간단한 웹 애플리케이션입니다. 이 프로젝트는 Django 프레임워크를 기반으로 개발되었습니다.
## 목차
- [설치](#설치)
- [사용법](#사용법)
- [기능](#기능)
- [프로젝트 구조](#프로젝트-구조)
- [기술 스택](#기술-스택)
- [기여 방법](#기여-방법)
- [라이선스](#라이선스)
## 설치
 - 파이썬 3.10 버전 설치 https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe
### 요구 사항
- Python 3.10
- Django 4.2
- SQLite (기본 데이터베이스)
- pillow 10.4.0
### 설치 단계
1. **프로젝트 클론하기**
   git clone https://github.com/DoosamGwak/Django_team_project.git
   cd Django_team_project
2. **가상환경 설정**
    python -m venv venv
    source venv/bin/activate  # 윈도우의 경우 `venv\Scripts\activate`
3. **필요한 패키지 설치**
    pip install -r requirements.txt
4. **데이터베이스 마이그레이션**
    python manage.py migrate  # 마이그레이션이 없는경우 생성 `python manage.py makemigrations`
5. **애플리케이션 실행**
    python manage.py runserver
이제 브라우저에서 http://127.0.0.1:8000/에 접속하여 애플리케이션을 확인할 수 있습니다.
## 사용법
1. **회원가입 및 로그인**
    사용자 계정을 만들고 로그인하여 판매할 제품을 게시 할 수 있습니다.
2. **제품 게시**
    로그인한 사용자는 판매할 제품을 등록할 수 있습니다. 제품 게시글에는 제목, 설명, 작성자 이름, 해시태그 등을 포함 할 수 있습니다.
3. **제품 검색**
    검색 창에 키워드를 입력하여 제품의 제목, 설명, 작성자 이름, 해시태그를 기준으로 제품을 검색 할 수 있습니다.
4. **팔로우 및 제품 찜하기**
    사용자는 서로 팔로우를 설정할 수 있으며, 각 제품에 대해 찜하기를 누를 수 있습니다.
5. **정렬 기능**
    최신순, 좋아요순, 조회수순으로 제품을 정렬하여 볼 수 있습니다.
## 기능
1. **사용자 인증**
    회원가입, 로그인, 로그아웃, 회원 탈퇴
2. **제품 게시**
    제품 등록, 수정, 삭제
3. **검색 기능**
    제목, 내용, 작성자, 해시태그, 찜하기를 통한 검색
4. **정렬 기능**
    최신순, 좋아요순, 조회수순 정렬
5. **제품 찜하기 기능**
    판매 상품에 찜하기
6. **유저 팔로우, 팔로잉 기능**
    유저들간 팔로우 및 팔로잉
## ERD
![image](https://github.com/user-attachments/assets/9e7d9149-e7e2-4a2a-b714-970aa7bd6f8d)
## 기술 스택
- 프로그래밍 언어  : Python 3.10
- 프레임워크  : Django 4.2
- 데이터베이스 : SQLite(개발 환경)
- 스타일링 : Bootstrap 5
- 아이콘 : Font Awesome
## 기여 방법
1. 프로젝트를 포크 합니다.
2. 새 브랜치를 만듭니다 (git checkout -b feature/기능-이름).
3. 변경 사항을 커밋합니다 (git commit -m 'Add some feature').
4. 브랜치에 푸시합니다 (git push origin feature/기능-이름).
5. 풀 리퀘스트를 생성합니다.
