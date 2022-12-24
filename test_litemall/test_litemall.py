"""
---------------------------
@Project: python_web_auto_project 
@Filename: test_litemall 
@Time: 2022/12/21 13:41
@Auther: dancing
@Email: 18623572576@163.com
---------------------------
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLitemall:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://litemall.hogwarts.ceshiren.com/#/dashboard")
        self.driver.find_element(By.CSS_SELECTOR, "[name=username]").clear()
        self.driver.find_element(By.CSS_SELECTOR, "[name=username]").send_keys('hogwarts')
        self.driver.find_element(By.CSS_SELECTOR, "[name=password]").clear()
        self.driver.find_element(By.CSS_SELECTOR, "[name=password]").send_keys('test12345')
        self.driver.find_element(By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--mini").click()
        time.sleep(5)

    def test_add_goods(self):
