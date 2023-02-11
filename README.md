# WBU自动健康打卡
## 开源地址：https://github.com/Xingsandesu/WBUdaka
## 博客链接：https://kookoo.top/
## 联系方式：1021461238@qq.com
## Python版本 3.11
## selenium版本 4.8
## WBU打卡 最新版本 1.3

# 相关运行库：
- requests
- os
- json
- schedule
- webdriver
- NoSuchElementException
- Service
- By
- ChromeDriverManager
- logging

# 使用方法：

- step1：安装好Python并配置好环境变量
- step2：安装好运行库
- step3：打开源码填写账号密码
- step4：按需求填入对应的Xpath，修改文本描述
- step5：填入企业微信推送相关信息
- step5：双击脚本运行

# Update list：
### 1.0beta
- 完成基础程式调用
### 1.0
- 添加判断语句
### 1.1
- 修改报错提示
- 缺少运行库直接弹出指令
- 优化运行速度
- 默认添加企业微信推送(自行配置企业微信)
### 1.2
- 设置默认窗口大小为Max
- 添加填报信息完成后或者报错时，自动向企业微信转发屏幕内容
### 1.3
- 浏览器调用初始化默认设置为无界面，以避免在该脚本运行在Windows服务器上关闭RDP后无法正常初始化浏览器
- 程序运行时现在会自动向企业微信发送消息
- 添加日志系统

# 未来更新计划:
- POM支持
- ~~- 辅导猫每日查寝自动签到~~

# memo
- Windows Server系统挂载本脚本时，如果遇到第二天无法自动打卡的情况，请尝试使用以管理员身份运行（So WIndows Fxxk U！）
- Linux下该脚本理论可用，具体请实际测试，本人未对Linux测试
- 由于学校暂不进行辅导猫查寝，辅导猫查寝更新 弃坑


# 成功范例
![范例.png](https://kookoo.top/usr/uploads/2023/02/2366700625.png)

