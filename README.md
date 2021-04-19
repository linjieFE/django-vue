# django-vue 前后端分离
  -  以blog为例CRUD
## 技术栈
 * django
 * django rest framework
 * django cors headers
##  前端 
 * vue
  
# 后端 步骤
* step1 初始化项目
 ```bash
 django-admin startproject backend
 ```
* step 2
```bash
cd backend
```
* step 3
```bash
 python manage.py runserver
```
* step4 刷新浏览器

```bash
 django-admin startapp blog
```
* 添加blog的Model，并添加一些初始数据
    1. 修改  `blog/models.py`
    2. 创建 model
    3. 修改 `backend/settings.py` 增加`blog` 再运行` python manage.py makemigrations`
      ```
      INSTALLED_APPS = [
          'django.contrib.admin',
          ...
          'blog',
      ]
      ```
    4. 运行 `python manage.py migrate`
    5. 运行 `python manage.py shell` 终端 键入 `from blog.models import Blog`
    6. 手动添加数据 `Blog.objects.create(title='b1',content='b1 content')`,`Blog.objects.all()`
    

* 使用 restframework 来添加 serializer, viwewset,urls
  - 官方文档[https://www.django-rest-framework.org/](rest-framework)
  1. 安装 `restframework` 到跟目录 第一层·backend· 下 `pip install djangorestframework`
  2. 修改 `backend/settings.py` 增加`rest_framework`
  3. blog 目录下 新建 `serializers.py`
  ```bash
    INSTALLED_APPS = [
      ...
      'rest_framework'
      'blog',
    ]
  ```
* 设置 跨域 cors headers

# 前端 
* vue cli
* 修改核心组件
* 添加 axios http 请求组件
* 添加 请求后组代码
