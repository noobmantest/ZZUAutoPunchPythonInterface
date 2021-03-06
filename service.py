import flask
from flask import request
import auto_punch_ZZU

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    # 获取通过url请求传参的数据
    user = request.values.get('user')
    # 获取url请求传的密码，明文
    password = request.values.get('password')
    # 密码和账号非空
    print(user, password)
    if user and password:
        res = auto_punch_ZZU.auto_punch(user, password)
        print(res)
        return res
    else:
        return "账号或密码为空"
    return "上报失败"


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
