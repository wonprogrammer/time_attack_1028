# 장고 심화 타임어택

# 목표

### 장고 심화 문법에 대해 이해하기

# 요구사항

## 요청 / 응답에 대한 부분은 모두 postman을 사용해 작성해주세

### 1. 프로젝트 폴더를 생성하고 가상 환경을 생성 및 실행 해주세요

### 2. djangorestframework와 djangorestframework-simplejwt패키지를 설치하고, requirements.txt에 설치 된 패키지를 저장해주세요

### 3. django_**advance**라는 이름으로 django 프로젝트를 생성해주세요

### 4. github에  새로운 리포지토리를 생성해주세요

### 5.  .gitignore 설정 후 django_**advance** 프로젝트를 푸시해주세요

### 6. settings.py에 jwt토큰을 사용할 수 있도록 설정해주세요

- code
    
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication'
        ]
    }
    ```
    

### 7. urls.py에 jwt 로그인 url을 지정해주세요

- code
    
    ```python
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    ```
    

### 8. article 앱을 만들고 settings.py에 등록해주세요

### 9. article의 models.py에  Article 모델을 생성해주세요.

- **요구조건**
    - author라는 필드를 foreignkey로 지정하고, user model을 참조하도록 해주세요
    - title이라는 필드를 charfield로 지정해주세요
    - content라는 필드를 textfield로 지정해주세요

### 10. article에 serializers.py 파일에 ModelSerializer를 사용해 시리얼라이저를 생성하고 Article 모델을 지정해주세요

### 11. article 앱의 의 views.py에 APIView를 사용해 get / post 요청을 받을 수 있는 ArticleView 클래스를 만들고

### 12. 프로젝트 urls에 /api/article/ 경로로 접속했을 때 article의 urls를 호출하도록 설정하고, article의 urls.py에 ‘’ 경로로 접속했을 때 ArticleView를 호출하도록 설정해주세요

### 13. ArticeView에 post 요청을 받으면 serializer를 사용해 로그인 한 사용자를 author로 지정하고 게시글을 생성할 수 있도록 해주세요

### 14. ArticeView에 get 요청을 받으면 serializer를 사용해 모든 게시글 목록을 리턴하도록 해주세요

### 15. postman으로 테스트를 진행해주세요

- **로그인(python manage.py createsuperuser로 계정 생성)**
    
    ```json
    // 요청 예제
    {
        "username": "계정",
        "password": "비밀번호"
    }
    
    // 응답 예제
    {
        "refresh": "리프레시 토큰",
        "access": "엑세스 토큰"
    }
    ```
    
- **게시글 작성**
    
    ```json
    // 요청 예제(POST)
    {
        "title": "제목",
        "content": "내용"
    }
    
    // 응답 예제
    {
        "id": 1,
        "title": "제목",
        "content": "내용",
        "author": 1
    }
    ```
    
- **게시글 조회**
    
    ```json
    // 요청 예제(GET)
    {}
    // 응답 예제
    [
        {
            "id": 1,
            "title": "제목",
            "content": "내용",
            "author": 1
        },
        {
            "id": 2,
            "title": "제목",
            "content": "내용",
            "author": 1
        },
        {
            "id": 3,
            "title": "제목",
            "content": "내용",
            "author": 1
        }
    ]
    ```
    

### 16. 테스트 결과를 확인하고 작업 내용들을 메인 브랜치에 푸시 해주세요
