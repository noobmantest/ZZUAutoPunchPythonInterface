from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import selenium.common.exceptions as selenium_exceptions
import time

def auto_punch(user, password):
    print("*" * 10, "启动脚本开始打卡", "*" * 10, user, "*" * 10)
    options = Options()
    # 设置无界面运行
    # options.add_argument('--headless')
    # 设置跳过不支持TLS1.0页面
    options.set_preference("security.tls.version.min", 1)
    # driver = webdriver.Firefox(executable_path=r'/usr/firefox/geckodriver',options=options)
    driver = webdriver.Firefox(executable_path=r'C:\Users\gzc\Desktop\upload\geckodriver.exe', options=options)

    try:
        try:
            time.sleep(5)
            driver.get(r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0')  # 健康打卡平台
        except selenium_exceptions.WebDriverException:
            driver.quit()
            print("加载页面失败，推断网络问题")
            return "NetworkProblems"
        print("加载登录页面成功")
        # chrome 跳过安全页面
        # details_button=driver.find_element_by_id('details-button')
        # details_button.click()
        # ele = driver.find_element_by_link_text('继续前往jksb.v.zzu.edu.cn（不安全）')
        # ele.click()

        driver.implicitly_wait(30)

        confirm_code = driver.find_element_by_xpath('/html/body/form/div/div[2]/div[4]/div[2]')  # 获取验证码块
        if confirm_code.text == "验证码":
            print("弹出验证码")
            driver.quit()  # 退出驱动并关闭所有关联窗口
            return "verificationCode"
        driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys(user)  # 输入账号
        driver.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys(password)  # 输入密码
        driver.find_element_by_xpath('//*[@id="mt_5"]/div[5]/div/input').click()  # 点击登录

        # 密码错误情况判断，如果找不到本人填报字样推测账号或密码有误
        try:
            driver.switch_to.frame("zzj_top_6s")
            print("登录成功")
            # driver.find_element_by_xpath('//*[@id="bak_0"]/div[13]/div[5]/div[4]').click()  # 点击本人填报
            driver.find_element_by_xpath('/html/body/form/div/div[13]/div[5]/div[4]').click()
            print("点击本人填报")
        except (selenium_exceptions.NoSuchElementException, selenium_exceptions.NoSuchFrameException):
            print("找不到本人填报按钮，推测账号或密码错误")
            driver.quit()
            return "accountOrPassword"

        driver.implicitly_wait(30)
        driver.find_element_by_xpath('//*[@id="bak_0"]/div[7]/div[4]').click()  # 点击提交表格

        driver.find_element_by_xpath('//*[@id="bak_0"]/div[2]/div[2]/div[4]/div[2]').click()  # 点击确定

        text = driver.find_element_by_xpath('//*[@id="bak_0"]/div[2]').text  # 获取成功提示
        print(text)
        if text == "已完成今日健康状况上报":
            print("上报成功")
        driver.quit()
        return "Success"

    except Exception as e:
        print("脚本异常")
        print(e)
        driver.quit()
        return "scriptException"
