## 框架
    FLASK
    SWAGGER
    Flask-RESTPlus
    
## 目录
    flask-rest-rbac
        app
            api
                controller          # api控制层
                    serializers.py  # 封装json参数格式化输出
                service             # api业务实现层
                __init__.py         # 设置Flask蓝图，托管API
            models                  # ORM数据库表映射
                models.py           # sqlacodegen 自动生成
            site                    # Swagger UI
            __init__.py             # 蓝图API注册，使用API命名空间，组织RESTful资源和HTTP
        config                      # 配置文件
            settings.py             # Flask配置，数据库配置等
        venv                        # python环境
        logging.conf                # 日志
        Pipfile                     # 包管理
        requirements.txt            # 依赖包以及版本号，便于新环境部署
        runserver.py                # 程序入口启动文件
    
    
## 工具
    sqlacodegen: 根据已有数据库生成ORM使用的models.py
    eg: sqlacodegen 'mysql+pymysql://root:123456@localhost:3306/testDB?charset=utf8' > app/models/models.py
    
    
## 技术点
    pipenv
    flask_restplus：
        api.namespace() 创建带有URL前缀的命名空间，description 描述方法
        eg: ns_user = Namespace(name='users', description='用户相关操作')
        @ns_user.route() 装饰指定网址关联资源
        marshal_with()装饰器接受你的数据对象，并对其按照model格式进行字段过滤
        Resource: 返回值转换成相应对象
        
    嵌套字段：
        relationship
        ForeignKey

    批量操作：
        db.session.flush()
    模型继承：
        menuElementOperation = api.inherit('Model menuElementOperation',  menu, {
            'elements': fields.List(fields.Nested(menuElement)),
            'operations': fields.List(fields.Nested(menuOperation))
        })
    分页paginate:
        paginate（page = None，per_page = None，error_out = True，max_per_page = None ）
        per_page从页面返回项目page。
        
        如果page或者per_page是None，他们将请求查询检索。如果max_per_page指定，per_page则将限制为该值。如果没有请求或它们不在查询中，则它们分别默认为1和20。
        
        如果error_out是True（默认），以下规则将导致404响应：
        
        没有找到任何物品，page也不是1。
        
        page小于1，或者per_page是负数。
        
        page或者per_page不是整数。
        
        当error_out是False，page并且per_page默认为分别为1和20。
    token认证：
        见参考文献flask之token认证,
        RESTFul扩展集成,decorators = [auth.login_required]
    response:
        jsonify直接返回的是Content-type:application/json的响应对象(Response对象)
        json.dumps返回的，则是Content-type:text/html,charset=utf-8的HTML格式
        
## log
    2019-08-14  添加.gitignore,删除多余文件
                修正DB.sql
                添加docker打包（启动命令：docker-compose up）
    
## 参考文献

[Flask 快速入门](http://docs.jinkan.org/docs/flask/quickstart.html# "悬停")

[Flask,Swagger UI 和 Flask-RESTlus构建REST API](http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)

[FlaskRESTful](http://www.pythondoc.com/Flask-RESTful/index.html)

[Flask-SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/index.html)

[flask之token认证](https://blog.csdn.net/ousuixin/article/details/94053454)