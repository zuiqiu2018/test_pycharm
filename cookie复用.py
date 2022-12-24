"""
---------------------------
@Project: python_web_auto_project 
@Filename: 浏览器复用 
@Time: 2022/12/21 16:40
@Auther: dancing
@Email: 18623572576@163.com
---------------------------
"""
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# # 访问扫码页面
# driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
# # 给20秒时间手动扫码
# time.sleep(40)
# # 扫码后获取cookie信息
# cookie = driver.get_cookies()
# print(cookie)
# # 把cookie存入一个可持久存储的地方
# with open("cookie.yaml", "w") as f:
#     yaml.safe_dump(cookie, f)
#
# driver.quit()
#
# 再次访问微信登录页
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")

# 从cookie文件中拿到cookie,并逐一植入
cookies = yaml.safe_load(open("cookie.yaml"))
for c in cookies:
    driver.add_cookie(c)
time.sleep(3)
# 再次访问微信登录页
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
time.sleep(3)


driver.find_element(By.CSS_SELECTOR, '.ww_indexImg.ww_indexImg_AddMember').click()
time.sleep(3)