

from app import create_app

app = create_app()



if __name__ == '__main__':
    app.run(port=5007)

# 注册登录
# 部署。yml, 不写成对应 json, 必须准备好测试所需要的所有的数据，存到 request, json,