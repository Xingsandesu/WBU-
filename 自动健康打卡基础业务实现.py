# Copyright (C) 2023 kodesu, Inc. All Rights Reserved
# @Time    : 2023-2
# @Author  : kodesu
# @Blog    : kookoo.top
# ————————————————
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def daka():
    """健康打卡基础业务代码实现"""
    global driver
    try:
        # 版本信息
        Ver = '1.0'
        print('Copyright (C) 2023 kodesu, Inc. All Rights Reserved ')
        print('Date    : 2023-2')
        print('Author  : kodesu')
        print('Blog    : https://kookoo.top')
        print(f"Ver     : {Ver}")
        print('本工具仅为学习用途，禁止商业化运用！')

        # 初始化驱动
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print('初始化成功！')

        # 设置用户信息变量
        User_id = ''
        User_pw = ''

        # 检查账号设置
        try:
            # 打开登录网页
            Web = 'http://wdt.wbu.edu.cn:9999/wxfwdt/html/wxfwdt/fwdt/wxfwdt.html#/'
            driver.get(Web)
            print('网页打开成功！')
            time.sleep(1)

            # 登录定位
            El_username = driver.find_element(By.ID, "username")
            El_password = driver.find_element(By.ID, "password")
            El_Login = driver.find_element(By.ID, "login_submit")
            print('登录信息定位成功！')
            print(f"账号:{User_id}")
            print(f"密码：{User_pw}")
            print(f"账号定位信息为：{El_username}")
            print(f"密码定位信息为：{El_password}")
            time.sleep(1)
            # 登录账号密码
            El_username.send_keys(User_id)
            El_password.send_keys(User_pw)
            time.sleep(1)
            El_Login.click()
            print('账号自动填入成功！')
            time.sleep(1)

            # 业务定位
            El_shangbao = driver.find_element(By.XPATH, '//*[@id="A1955352694A6ACAE0530100007F1F6F"]/div')
            El_jilu = driver.find_element(By.XPATH, '//*[@id="A2D6B7D8CBDA4D9AE0530100007FC0C1"]/div')
            El_shangbao.click()
            print('健康上报界面开启成功！')
            print(f"业务定位信息为：{El_shangbao}")
            time.sleep(2)

            # 到校信息填报
            El_daoxiao = driver.find_element(By.XPATH, '//*[@id="k1"]/div[2]/label')
            El_weidaoxiao = driver.find_element(By.XPATH, '//*[@id="k1"]/div[1]/label')
            El_daoxiao.click()
            print('到校信息录入成功,目前状态为到校')
            print(f"到校信息定位信息为：{El_daoxiao}")
            time.sleep(1)

            # 到校体温信息填报
            El_tiwen = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[7]/div[1]/div[2]/input')
            Tiwen = '37'
            El_tiwen.send_keys(Tiwen)
            print(f"体温信息录入成功,数值为{Tiwen}")
            print(f"体温定位信息为：{El_tiwen}")
            time.sleep(1)

            # 未到校地址信息填报
            # Dizhi = ''
            # El_suozaidi = driver.find_element(By.XPATH, '//*[@id="start"]')
            # El_dizhi = driver.find_element(By.XPATH, '//*[@id="jzddzDiv"]/div[2]/input')
            # El_dizhi.send_keys(Dizhi)
            # print(f"地址信息填报成功,目前地址为{Dizhi}")
            # print(f"所在地信息定位信息为：{El_suozaidi}")
            # print(f"地址信息定位信息为：{El_dizhi}")
            # time.sleep(1)

            # 状态信息XPath
            # 已感染已转阴 //*[@id="sqbJkxx-dataForm"]/div[9]/div/div[1]/label
            # 已感染未转阴 //*[@id="sqbJkxx-dataForm"]/div[9]/div/div[2]/label
            # 尚未感染 //*[@id="sqbJkxx-dataForm"]/div[9]/div/div[3]/label
            El_zhuangtai = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[9]/div/div[1]/label')
            El_zhuangtai2 = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[9]/div/div[2]/label')
            El_zhuangtai3 = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[9]/div/div[3]/label')
            El_zhuangtai.click()
            print('状态信息填报成功，目前状态是：已感染已转阴')
            print(f"状态信息1定位信息为：{El_zhuangtai}")
            print(f"状态信息2定位信息为：{El_zhuangtai2}")
            print(f"状态信息3定位信息为：{El_zhuangtai3}")
            time.sleep(1)

            # 同居状态信息Xpath
            # 已感染已转阴 //*[@id="tzrygrqk"]/div[1]/label
            # 已感染未转阴 //*[@id="tzrygrqk"]/div[2]/label
            # 尚未感染 //*[@id="tzrygrqk"]/div[3]/label
            # 其他情况 //*[@id="tzrygrqk"]/div[4]/label
            El_tongju_zhuangtai = driver.find_element(By.XPATH, '//*[@id="tzrygrqk"]/div[1]/label')
            El_tongju_zhuangtai2 = driver.find_element(By.XPATH, '//*[@id="tzrygrqk"]/div[2]/label')
            El_tongju_zhuangtai3 = driver.find_element(By.XPATH, '//*[@id="tzrygrqk"]/div[3]/label')
            El_tongju_zhuangtai4 = driver.find_element(By.XPATH, '//*[@id="tzrygrqk"]/div[4]/label')
            El_tongju_zhuangtai.click()
            print('同居状态信息填报成功，目前同居状态信息是：已感染已转阴')
            print(f"同居状态信息1定位信息为：{El_tongju_zhuangtai}")
            print(f"同居状态信息2定位信息为：{El_tongju_zhuangtai2}")
            print(f"同居状态信息3定位信息为：{El_tongju_zhuangtai3}")
            print(f"同居状态信息4定位信息为：{El_tongju_zhuangtai4}")
            time.sleep(1)

            # 承诺
            El_chengnuo = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[14]/label')
            El_chengnuo.click()
            print('承诺已填报')
            print(f"承诺定位信息为：{El_chengnuo}")
            time.sleep(1)

            # 提交
            El_tijiao = driver.find_element(By.XPATH, '//*[@id="qrtj"]')
            El_tijiao.click()
            print('上报信息已提交')
            print('5秒后自动退出程序')
            print('健康上报填报完毕!')
            time.sleep(5)
            driver.quit()
        except NoSuchElementException:
            driver.quit()
            print('账号密码错误，请填入正确的账号密码')
            print('认证失败')
            time.sleep(10)
    except NoSuchElementException:
        driver.quit()
        print('找不到Xpath')
        print('已打卡或系统更新，如未打卡出现该消息请联系作者')
        print('邮箱：1021461238@qq.com')
        time.sleep(10)



if __name__ == '__main__':
    daka()
