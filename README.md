# Blog
可以评论的博客系统
使用Python的django框架编写，部署在heroku，网址为：https://frl-blog.herokuapp.com/
有博客和todolist两个应用
若要在本地运行，需要修改setting数据库配置如下：
取消注释
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
注释
'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
