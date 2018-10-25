# django_practice

## 패키지 구조
* django1
    * __init__.py : 디렉토리르 파이썬 패키지로 지정
    * settings.py : 장고 환경 설정
    * urls.py : 장고 URL 선언, 다른 app의 urls.py를 import하여 URL 맵핑을 할 수 있다.
    * wsig.py : WSIG 호환 Web Server의 entry point 정의
* app1
    * __init__.py : 디렉토리르 파이썬 패키지로 지정
    * models.py : 모델 설정
    * views.py web view 파일 설정
    * urls.py : URL 선언
* templates
    * template files
   
## conda 환경 
### 라이브러리 모듈 설치

```
$ cd ${PROJECT_HOME}/envs/
$ conda env create -f python3.6-environment.yml
```


### 라이브러리 모듈 업데이트

```
$ cd ${PROJECT_HOME}/envs/
$ conda env update -f python3.6-environment.yml
```

## requisites
* miniconda : https://conda.io/miniconda.html
