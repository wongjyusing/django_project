### 说明  
这次项目的配置按照真正的项目来配置。  
之前**最简单的博客**的项目配置方法只是用来练手的。  
这次需要我们重新创建一个新的项目来进行学习。  
### 创建项目  
找个新的目录来创建项目，把之前的项目放到其它地方也行。   
注意，确保下面的步骤在**虚拟环境**中进行。  
依次在终端下执行下面的代码。  
```bash
django-admin startproject mysite

cd mysite

python manage.py startapp blog

mkdir static templates apps

mkdir blog/templates

mkdir blog/static   

mkdir blog/static/css

mkdir blog/static/js

mkdir blog/templatetags

touch blog/templatetags/__init__.py

touch blog/templatetags/blog_tags.py

touch blog/urls.py                  

mv blog apps
```
这个时候目录结构如下：
```bash
.
├── apps
│   └── blog
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── static
│       │   ├── css
│       │   └── js
│       ├── templates
│       ├── templatetags
│       │   ├── blog_tags.py
│       │   └── __init__.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
└── templates

12 directories, 17 files

```  
想偷懒的话可以使用。  
