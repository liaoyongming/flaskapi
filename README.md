# flaskapi
## flask +flask_restful +mysql

## 初始化数据库

在mysql中创建schema your_schema

`config.py`文件中配置数据库连接`    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://username:pwd@www.example.com/your_schema'  `

执行

`python manage.py db init`

`python manage.py db migrate`

`python manage.py db upgrade`

