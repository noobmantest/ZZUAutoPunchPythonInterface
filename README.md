# ZZUAutoPunchPythonInterface
郑州大学健康打卡python脚本，提供接口访问

## 右上角start支持一下，一定要点哦
 关键代码在 auto_punch_ZZU.py 中，  
 调用def auto_punch(user, password)方法，传入用户名和密码

service.py用于提供访问接口


## 更新目前位置信息
使用request包发送相应请求,参考service_requests.py  
提供打卡接口, 参考auto_punch_ZZU_requests.py

## 更新解决详细位置中文乱码问题
使用post方式接收json格式数据，
data = request.get_data()
解析json字符串
j_data = json.loads(data)
获取数据
j_data('password')



# 前端页面地址 http://81.70.250.230:8081/autoPunch/#/

