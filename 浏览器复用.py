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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.ww_indexImg.ww_indexImg_AddMember').click()
time.sleep(3)