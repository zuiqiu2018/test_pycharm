from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

# element_to_be_clickable的返回是webelements对象，所以可以接click()，但不是所有的expected_conditions返回的都是webelements对象，具体要看源码
WebDriverWait(driver, 10, 1).until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn'))).click()
driver.quit()

expected_conditions.element_to_be_clickable()
expected_conditions.visibility_of_element_located()
expected_conditions.url_contains()
expected_conditions.title_is()
expected_conditions.frame_to_be_available_and_switch_to_it()
expected_conditions.alert_is_present()


def element_to_be_clickable(target_element, next_element):
    """
    :param target_element:点击的目标按钮
    :param next_element:下一个页面的某个元素
    :return:
    """

    def _predicate(driver):
        driver.find_element(*target_element).click()
        # 第一种结果为找到，return的内容为element对象
        # 第二种结果，没有找到，until会抛出异常
        return driver.find_element(*next_element)

    return _predicate
