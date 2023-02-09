# Copyright (C) 2023 kodesu, Inc. All Rights Reserved
# @Time    : 2023-2
# @Author  : kodesu
# @Blog    : kookoo.top
# ————————————————
import os
import time
import json
import requests
import schedule
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import logging

# 时间格式化
current_time = int(time.time())
localtime = time.localtime(current_time)
date = time.strftime('%Y:%m:%d %H:%M:%S', localtime)


def wbudaka():
    """健康打卡基础业务代码实现"""
    try:
        # 版本信息
        Ver = '1.3'
        print('Copyright (C) 2023 kodesu, Inc. All Rights Reserved ')
        print('Date    : 2023-2')
        print('Author  : kodesu')
        print('Blog    : https://kookoo.top')
        print(f"Ver     : {Ver}")
        print('本工具仅为学习用途，禁止商业化运用！')
        print('--------------------')

        # 初始化浏览器调用
        # 无界面模式
        service = ChromeService(executable_path=ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options, service=service)
        logprint.info('武汉商学院自动健康打卡初始化成功！')

        # 设置最大化窗口
        driver.maximize_window()

        # 设置用户信息变量
        User_id = ''
        User_pw = ''

        # 检查账号设置
        try:
            # 打开登录网页
            Web = 'http://wdt.wbu.edu.cn:9999/wxfwdt/html/wxfwdt/fwdt/wxfwdt.html#/'
            driver.get(Web)
            logprint.info('网页打开成功！')
            time.sleep(1)

            # 登录定位
            El_username = driver.find_element(By.ID, "username")
            El_password = driver.find_element(By.ID, "password")
            El_Login = driver.find_element(By.ID, "login_submit")
            logprint.info('登录信息定位成功！')
            logprint.info(f"账号:{User_id}")
            logprint.info(f"密码：{User_pw}")
            # print(f"账号定位信息为：{El_username}")
            # print(f"密码定位信息为：{El_password}")
            # 登录账号密码
            time.sleep(1)
            El_username.send_keys(User_id)
            time.sleep(1)
            El_password.send_keys(User_pw)
            time.sleep(1)
            El_Login.click()
            logprint.info('账号自动填入成功！')
            driver.implicitly_wait(10)

            # 业务定位
            El_shangbao = driver.find_element(By.XPATH, '//*[@id="A1955352694A6ACAE0530100007F1F6F"]/div')
            El_jilu = driver.find_element(By.XPATH, '//*[@id="A2D6B7D8CBDA4D9AE0530100007FC0C1"]/div')
            El_shangbao.click()
            logprint.info('健康上报界面开启成功！')
            # print(f"业务定位信息为：{El_shangbao}")
            driver.implicitly_wait(10)

            # 到校信息填报
            El_daoxiao = driver.find_element(By.XPATH, '//*[@id="k1"]/div[2]/label')
            El_weidaoxiao = driver.find_element(By.XPATH, '//*[@id="k1"]/div[1]/label')
            El_daoxiao.click()
            logprint.info('到校信息录入成功,目前状态为到校')
            # print(f"到校信息定位信息为：{El_daoxiao}")

            # 到校体温信息填报
            El_tiwen = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[7]/div[1]/div[2]/input')
            Tiwen = '37'
            El_tiwen.send_keys(Tiwen)
            logprint.info(f"体温信息录入成功,数值为{Tiwen}")
            # print(f"体温定位信息为：{El_tiwen}")

            # 未到校地址信息填报
            # Dizhi = ''
            # El_suozaidi = driver.find_element(By.XPATH, '//*[@id="start"]')
            # El_dizhi = driver.find_element(By.XPATH, '//*[@id="jzddzDiv"]/div[2]/input')
            # El_dizhi.send_keys(Dizhi)
            # print(f"地址信息填报成功,目前地址为{Dizhi}")
            # print(f"所在地信息定位信息为：{El_suozaidi}")
            # print(f"地址信息定位信息为：{El_dizhi}")

            # 状态信息XPath
            # 已感染已转阴 //*[@id="sqbJkxx-dataForm"]/div[9]/div/div[1]/label
            # 已感染未转阴 //*[@id="sqbJkxx-dataForm"]/div[9]/div/div[2]/label
            # 尚未感染 //*[@id="sqbJkxx-dataForm"]/div[9]/div/div[3]/label
            El_zhuangtai = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[9]/div/div[1]/label')
            El_zhuangtai2 = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[9]/div/div[2]/label')
            El_zhuangtai3 = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[9]/div/div[3]/label')
            El_zhuangtai.click()
            logprint.info('状态信息填报成功，目前状态是：已感染已转阴')
            # print(f"状态信息1定位信息为：{El_zhuangtai}")
            # print(f"状态信息2定位信息为：{El_zhuangtai2}")
            # print(f"状态信息3定位信息为：{El_zhuangtai3}")

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
            logprint.info('同居状态信息填报成功，目前同居状态信息是：已感染已转阴')
            # print(f"同居状态信息1定位信息为：{El_tongju_zhuangtai}")
            # print(f"同居状态信息2定位信息为：{El_tongju_zhuangtai2}")
            # print(f"同居状态信息3定位信息为：{El_tongju_zhuangtai3}")
            # print(f"同居状态信息4定位信息为：{El_tongju_zhuangtai4}")

            # 承诺
            El_chengnuo = driver.find_element(By.XPATH, '//*[@id="sqbJkxx-dataForm"]/div[14]/label')
            El_chengnuo.click()
            logprint.info('承诺已填报')
            # print(f"承诺定位信息为：{El_chengnuo}")

            # 提交
            El_tijiao = driver.find_element(By.XPATH, '//*[@id="qrtj"]')
            El_tijiao.click()
            logprint.info("健康打卡完毕")
            time.sleep(1)
            driver.get_screenshot_as_file("健康已打卡.png")
            send_text_message(f"{date}健康打卡完毕")
            send_picture_message(get_media_id("image", "健康已打卡.png"))
            time.sleep(2)
            driver.quit()
        except NoSuchElementException:
            logprint.error("健康打卡账号密码错误或已打卡，请确认账号密码是否正确或系统选项更新")
            driver.get_screenshot_as_file("健康未打卡.png")
            send_text_message(f"{date}健康打卡账号密码错误或已打卡，请确认账号密码是否正确或系统选项更新")
            send_picture_message(get_media_id("image", "健康未打卡.png"))
            driver.quit()
            time.sleep(2)
    except ModuleNotFoundError:
        logprint.error('相关依赖未安装，请运行以下命令安装相关库')
        print('相关依赖未安装，请运行以下命令安装以下相关库')
        print('pip install webdriver-manager')
        print('pip install requests')
        print('pip install schedule')
        print('pip install json')
        print('pip install time')
        print('--------------------')
        send_text_message(f"{date}相关依赖未安装，请安装相关库")
        time.sleep(5)


# 企业微信推送消息函数信息设置
corpid = ""  # 企业id值
corpsecret = ""  # 应用secret值


# 企业微信推送文本消息
def send_text_message(message):
    send_text_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(get_access_token())
    data = {
        "touser": "@all",  # 接收消息的用户
        "msgtype": "text",  # 消息类型
        "agentid": 1000002,  # 应用id
        "text": {
            "content": message  # 消息内容
        },
        "safe": 0,  # 0为公开信息，1为保密信息
    }
    text_message_res = requests.post(url=send_text_url, data=json.dumps(data)).json()
    return text_message_res


# 企业微信推送图片消息-上传临时素材并获取media_id
def get_media_id(filetype, path):
    upload_file_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}".format(
        get_access_token(), filetype)
    files = {filetype: open(path, 'rb')}
    file_upload_result = requests.post(upload_file_url, files=files).json()
    return file_upload_result["media_id"]


# 企业微信推送图片消息
def send_picture_message(media_id):
    send_picture_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(get_access_token())
    data = {
        "touser": "@all",
        "msgtype": "image",
        "agentid": 1000002,
        "image": {
            "media_id": media_id
        },
        "safe": 0,
    }
    picture_message_res = requests.post(url=send_picture_url, data=json.dumps(data)).json()
    return picture_message_res


# 企业微信获取token
def get_access_token():
    get_act_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(corpid, corpsecret)
    act_res = requests.get(url=get_act_url).json()
    access_token = act_res["access_token"]
    return access_token




# 辅导猫查寝签到(待更新)
def wbuchaqin():
    # 初始化浏览器调用
    service = ChromeService(executable_path=ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    logprint.info('辅导猫打卡初始化成功！')


# 日志系统

class Logger():
    def __init__(self):
        # 创建一个日志器
        self.logger = logging.getLogger("logger")

        # 设置日志输出的最低等级,低于当前等级则会被忽略
        self.logger.setLevel(logging.INFO)

        # 创建处理器：sh为控制台处理器，fh为文件处理器
        sh = logging.StreamHandler()

        # 创建处理器：sh为控制台处理器，fh为文件处理器,log_file为日志存放的文件夹
        log_file = os.path.join("autotest.log")
        fh = logging.FileHandler(log_file, mode="a", encoding="UTF-8")

        # 创建格式器,并将sh，fh设置对应的格式
        formator = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s",
                                     datefmt="%Y/%m/%d %X")
        sh.setFormatter(formator)
        fh.setFormatter(formator)

        # 将处理器，添加至日志器中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)


logprint = Logger().logger


# 每日任务循环实现
if __name__ == '__main__':
    try:
        timeset = "07:00"
        logprint.info(f"脚本启动成功,运行时间设置为每天{timeset}")
        send_text_message(f"{date}脚本启动成功,运行时间设置为每天{timeset}")
        schedule.every().day.at(timeset).do(wbudaka)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logprint.error(f"{date}脚本被手动关闭！")
        send_text_message(f"{date}脚本被手动关闭！")
