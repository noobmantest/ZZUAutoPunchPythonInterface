import flask
from flask import request
import auto_punch_ZZU_requests
import json
from tools import log

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
    try:
        log.write_log('收到请求，开始执行')
        # 获取字符串json格式，使用post请求
        data = request.get_data()
        j_data = json.loads(data)  # 解析json字符串
        log.write_log('接收请求数据 ==== ' + str(j_data))

        user_account = j_data['user']
        pwd = j_data['password']
        city_code = j_data['city_code']
        address = j_data['address']

        log.write_log('开始执行脚本')
        res = auto_punch_ZZU_requests.auto_punch(user_account, pwd, city_code, address)
        log.write_log('脚本执行结果 === ' + res)
        return res
    except Exception as e:
        print(e)
        log.write_log('执行失败 ==== ' + str(e))
        return 'failPunch'
    else:
        return 'failPunch'


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
