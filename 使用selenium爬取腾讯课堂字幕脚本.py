import random
import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 使用以及存在的用户缓存打开chrome浏览器
profile_directory = r'--user-data-dir=C:\Users\10598\AppData\Local\Google\Chrome\User Data'
option = ChromeOptions()
option.add_argument(profile_directory)
webdriver = webdriver.Chrome(chrome_options=option)
webdriver.get('https://ke.qq.com/')
# time.sleep(2)
# login_btn = webdriver.find_element(by='xpath', value='//div[@class="btn"]')
# login_btn.click()
# time.sleep(2)
#
# agree_checkbox = webdriver.find_element(by='xpath', value='//i[@class="kecomp-checkbox-icon"]')
# agree_checkbox.click()
# time.sleep(2)
#
# login_btn_qq = webdriver.find_element(by='xpath', value='//button[@class="login-btn qq-btn"]')
# login_btn_qq.click()
# time.sleep(5)


from selenium.webdriver.common.action_chains import ActionChains


# ActionChains(webdriver).move_by_offset(250,500).click().perform()
# login_iframe = webdriver.find_element(by='xpath', value='//iframe[@title="qq账号登录"]')
# webdriver.switch_to.frame(login_iframe)
# login_btn_qq_user_image = webdriver.find_element(by='xpath', value='//span[@class="nick" and @id="nick_1059880026"]')
# login_btn_qq_user_image.click()
# time.sleep(4)

# webdriver.switch_to.default_content()

my_class_sche = webdriver.find_element(by='xpath', value='//div[@class="btn" and text()="我的课表"]')
my_class_sche.click()
time.sleep(2)

play = webdriver.find_element(by="xpath", value='//span[text()="看录播"]')
play.click()
time.sleep(3)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


handles = webdriver.window_handles
webdriver.switch_to.window(handles[-1])
time.sleep(3)
WebDriverWait(webdriver, 6000).until(EC.presence_of_element_located((By.XPATH, '//button[@class="loki-interact loki-menu-button loki-rate-button" and text()="1x"]'))) # 60s
# ActionChains(webdriver).move_by_offset(250,500).click().perform()
# speed_btn = webdriver.find_element(by='xpath', value='//button[@class="loki-interact loki-menu-button loki-rate-button" and text()="1x"]')
# speed_btn.click()
# webdriver.find_element(by="xpath", value='//li[text()="2x"]').click()
# ActionChains(webdriver).move_by_offset(250,500).click().perform()



last_text = ""
last_title = ""

# 自行计时
def jishi(st, et):
    ft = ""
    if et < 10:
        ft = "00:" + "0" + str(et)
    elif 10 <= et < 60:
        ft = "00:" + str(et)
    elif 600 > et >= 60:
        if et % 60 < 10:
            ft = "0" + str(int(et / 60)) + ":" + "0" + str(et % 60)
        elif et % 60 >= 10:
            ft = "0" + str(int(et / 60)) + ":" + str(et % 60)
    elif 3600 > et >= 600:
        if et % 60 < 10:
            ft = str(int(et / 60)) + ":" + "0" + str(et % 60)
        elif et % 60 >= 10:
            ft = str(int(et / 60)) + ":" + str(et % 60)
    elif 36000 > et >= 3600:
        if et % 60 < 10 and (int(et / 60) - 60) < 10:
            ft = "0" + str(int(et / 3600)) + ":" + "0" + str(int(et / 60) - 60) + ":" + "0" + str(et % 60)
        elif 10 <= (et % 60) and (int(et / 60) - 60) < 10:
            ft = "0" + str(int(et / 3600)) + ":" + "0" + str(int(et / 60) - 60) + ":" + str(et % 60)
        elif et % 60 >= 10 and (int(et / 60) - 60) >= 10:
            ft = "0" + str(int(et / 3600)) + ":" + str(int(et / 60) - 60) + ":" + str(et % 60)
        elif et % 60 < 10 and (int(et / 60) - 60) >= 10:
            ft = "0" + str(int(et / 3600)) + ":" + str(int(et / 60) - 60) + ":" + "0" + str(et % 60)
    return ft


# 外层循环，控制课程切换
while 1:
    time.sleep(2)
    # 使用谷歌插件video speed，使用pynput按键盘d进行三倍速播放
    from pynput.keyboard import Key, Controller

    keyboard = Controller()
    # 按住一个键
    keyboard.press('d')
    # 松开一个键d
    keyboard.release('d')

    print("是否完成5倍速度")


    # 1、移动鼠标，拿到当前播放时间
    ActionChains(webdriver).move_by_offset(500, 1000).perform()
    ActionChains(webdriver).reset_actions()

    # 2、获取时间
    # 当前课程时间进度条文本
    time_text = webdriver.find_element('xpath', '//div[@class="loki-time"]').text
    # 进度条课程时长
    total_time = time_text.split('/')[1].lstrip()
    print(total_time)
    # 进度条实时时间
    now_time = time_text.split('/')[0].rstrip()
    print(now_time)

    # 计时开始
    st = time.time()
    while 1:
        try:
            # 3、获取字幕
            WebDriverWait(webdriver, 6000).until(EC.presence_of_element_located((By.XPATH, '//div[@style="max-width: inherit;"]')))  # 60s
            text = webdriver.find_element(by='xpath', value='//div[@style="max-width: inherit;"]').text

            # 4、确认当前课程名
            title = webdriver.find_element('xpath', '//div[@class="current-task-name header-item"]').text
            if last_title == title:
                pass
            elif last_title != title:
                # 拼接markdown三级标题：###
                final_title = "### " + title
                with open('docker.md', "a", encoding="utf-8") as f:
                    f.write('\n')
                    f.write('\n')
                    f.write('\n')
                    f.write(final_title)
                    f.write('\n')

                    if last_title == "":
                        last_title = title
                        print(last_title)
                    elif last_title != "":
                        last_title = title
                        break
            # 5、拼接时间和字幕,倍速，所以要先乘以2
            final_text = "[" + jishi(st, round((time.time() - st) * 2)) + "/" + total_time + "]" + "     " + text
            if last_text == text:
                pass
            elif last_text != text:
                with open('docker.md', "a", encoding="utf-8") as f:
                    f.write(final_text)
                    f.write('\n')
                    last_text = text
                    print(final_text)

        except:
            continue


