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
    6. 手动添加数据 
    `Blog.objects.create(title='b1',content='b1 content')`,
    `Blog.objects.create(title='b2',content='b2 content')`
    `Blog.objects.all()`
    创建完后`exit()`退出 shell
    

* 使用 restframework 来添加 serializer, viwewset,urls
  - 官方文档[https://www.django-rest-framework.org/](rest-framework)
  - 点这里快速开始 -> [官方文档](https://www.django-rest-framework.org/tutorial/quickstart/#views)
  1. 安装 `restframework` 到跟目录 第一层·backend· 下 `pip install djangorestframework`
  2. 修改 `backend/settings.py` 增加`rest_framework`
  3. blog 目录下 新建 `serializers.py`
  4. 创建`viewset` 修改 `blog/views.py`
  ```bash
    INSTALLED_APPS = [
      ...
      'rest_framework'
      'blog',
    ]
  ```
  5. 添加 `router`
     - 修改`urls.py`文件 注册到总路由。运行`python manage.py runserver` 再访问`http://127.0.0.1:8000/api/blog`时可以看到blog页面
* 设置 跨域 cors headers
  1.  安装 `django-cors-headers` 到跟目录 第一层·backend· 下 `pip install django-cors-headers`
  2. [参考文献](cnblogs.com/daviddd/p/12051522.html)
   - 添加到`setting`的app中
    ```py
      INSTALLED_APPS = (
        ...
        'corsheaders',
        ...
      )
    ```
    - 添加中间件
    ```py
    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
      ...
      'corsheaders.middleware.CorsMiddleware',
      'django.middleware.common.CommonMiddleware',
      ...
    ]
    ```
# 前端 
* vue cli
 - `npm install @vue/cli -g`
 - `vue create frontend`
 - `npm run serve`
* 修改核心组件
  - [bootstrap4](https://v4.bootcss.com/docs/getting-started/introduction/)
  - [fontwasome 字体美化库](https://fontawesome.dashgame.com/)
* 添加 axios http 请求组件
* 添加 请求后组代码
