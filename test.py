
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains

# 使用浏览器的驱动，详情参考https://www.jianshu.com/p/1b63c5f3c98e
# driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')#驱动的绝对路径,Chrome就把Firefox换成Chrome
# driver.get(r'http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn')#兰州大学个人工作台

url = 'https://www.baidu.com'
options = Options()
options.add_argument('--headless')
# driver = webdriver.Firefox(executable_path=r'/usr/firefox/geckodriver',options=options)
driver = webdriver.Firefox(executable_path=r'C:\Users\gzc\Desktop\upload\geckodriver.exe', options=options)

driver.get(r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0')  # 兰州大学个人工作台

# details_button=driver.find_element_by_id('details-button')
# details_button.click()
# ele = driver.find_element_by_link_text('继续前往jksb.v.zzu.edu.cn（不安全）')
# ele.click()

driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys('20177720415')  # 输入账号
driver.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys('07024612')  # 输入密码
driver.find_element_by_xpath('//*[@id="mt_5"]/div[5]/div/input').click()  # 点击登录

driver.switch_to.frame("zzj_top_6s")
driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[5]/div[4]').click()  # 点击本人填报

driver.find_element_by_xpath('//*[@id="bak_0"]/div[7]/div[4]').click()  # 点击提交表格

driver.find_element_by_xpath('//*[@id="bak_0"]/div[2]/div[2]/div[4]/div[2]').click()  # 点击确定

text = driver.find_element_by_xpath('//*[@id="bak_0"]/div[2]').text  # 获取成功提示
print(text)
if text == "已完成今日健康状况上报":
    print("上报成功")

driver.quit()


def test_function(s):
    print(s + "测试方法。。。")