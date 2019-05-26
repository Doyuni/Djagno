# Django Project 만들기

## 가상환경(virtual env) 만들기

꼭 ! 아래 page에서 가상환경을 만들고 활성화한 후 단계를 진행해주세요.  
[가상환경 만들기](https://www.notion.so/doyuni/Virtual-Environment-f53375349fd74754a9b5d6687dd67827)

## 장고(django) 프로젝트 만들기

가상환경 이름: myvenv

**장고 설치하기**

    (myvenv)
    $ pip install django

**장고 프로젝트 만들기**

    (myvenv)
    $ django-admin startproject 프로젝트이름

**app 만들기** ( 하나의 큰 기능을 가지고 있는 부분이라고 생각하시면 됩니다.)

    (myvenv) ~/project
    $ python manage.py startapp app이름

**생성된 app을 프로젝트에 연결시켜주기** 
 **settings.py**  의 INSTALLED_APP에서 다음을 추가합니다.

    ## settings.py ##
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myapp.apps.MyappConfig',
    ]

"myapp 폴더 안에 있는 apps 파일에 있는 MyappConfig 클래스를 등록합니다." 

    ## apps.py ##
    from django.apps import AppConfig
    
    class MyappConfig(AppConfig):
        name = 'myapp'

**apps.py** 를 보시면 왜 저렇게 추가하는구나를 알 수 있을 겁니다.

**app 폴더에 templates 폴더 만들고 html 파일 만들기** (templates/home.html)

    <!DOCTYPE html>
    <html lang="kr">
    <head>
        <meta charset="UTF-8">
        <title>Django project</title>
    </head>
    <body>
        <p>안녕하세요</p>
    </body>
    </html>

프로젝트 구조 (app 이름: myapp)

    project  
    ├── myapp  
    │   ├── migrations  
    │   │   ├── __pycache__  
    │   │   │   └── __init__.cpython-37.pyc     
    │   │   └── __init__.py  
    │   ├── templates  
    │   │   └── home.html  
    │   ├── __init__.py  
    │   ├── admin.py  
    │   ├── apps.py  
    │   ├── models.py  
    │   ├── test.py  
    │   └── views.py  
    ├── myproject  
    │   ├── __pycache__  
    │   │   ├── __init__.cpython-37.pyc  
    │   │   └── settings.cpython-37.pyc  
    │   ├── __init__.py  
    │   ├── settings.py  
    │   ├── urls.py  
    │   └── wsgi.py  
    ├── db.sqlite3 
    └── manage.py  

프로젝트 구조를 보시면서 혼동되지 않도록 주의합니다. (37은 python3.7 의미)

**views.py** 에 함수 정의하기

    from django.shortcuts import render
    
    def home(request):
        return render(request, 'home.html')

render(request, 템플릿이름, optional: dict 객체 ) → 3개의 인자를 가질 수 있습니다.
일단은 이정도만 알고 넘어갑니다.

**이제 urls.py 에서 url을 추가해줍니다.**

    from django.contrib import admin
    from django.urls import path
    import myapp.views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', myapp.home, name="home"),
    ]

"아무것도 입력하지 않았을 때, myapp에 있는 views파일에 있는 home 함수를 호출합니다. url 즉 path의 이름은 home 입니다."

**서버 구동하기.**

    $ python manage.py runserver

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) 에서 home.html 에 맞게 page가 띄어졌는지 확인합니다.
서버를 구동하면 myproject/__pycache__ 에 urls.cpython~~ 과 wsgi.cpython~~ 이 생겼음을 알 수 있습니다.

 기본적인 세팅이 끝났습니다. 
이제 간단한 프로젝트를 만들어서 실습을 해보도록 하겠습니다.
