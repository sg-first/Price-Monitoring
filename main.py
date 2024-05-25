from selenium import webdriver # 从selenium库里引入驱动器模块，用于控制浏览器。
from selenium.webdriver.common.by import By # 定位需要用到by模块，譬如by name或者by ID或者byXpath
from selenium.webdriver.support.ui import WebDriverWait # 显示等待模块，用于提取动态网站的元素。
from selenium.webdriver.support import expected_conditions as EC#
import schedule # 计时器
import threading # 设置线程
import time # 间隔时间
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 蛇形排列处理
prelist = [4.7919,4.7876,4.7972]+[4.8300]*140+[4.8200]*140+[4.8400]*45+[4.8100]*44+[4.8481,4.8507,4.8482,4.8478,4.8490,4.8486,4.8471,4.8475]
sorted_prelist = sorted(prelist)
manuallist = []
for i in range(len(prelist)//2):
    manuallist.append(sorted_prelist [i])
    manuallist.append(sorted_prelist [-i-1])

def judge_ifnot_del():
    if len(manuallist) >= 1151:
        manuallist.pop(0)

def sendemail(list,current_price):
    sorted_list = list[:]
    sorted_list.sort()
    percentnum = sorted_list[6]
    percent = 6 / len(sorted_list)*100
    if current_price <= percentnum:
        msg_from = 'xxxx@163.com'
        password = 'xxxxx'
        msg_to = ['yyyy@qq.com']
        subject = '快！！！快鸭！！！！'
        content = f'赶紧下单鸭！！！！！！！！！\n当前价是{current_price}，已经小于{percent}%百分位价格{percentnum}'
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['from'] = formataddr(('陈一言你的贴心管家', msg_from))
        msg['to'] = ','.join(msg_to)
        try:
            s = smtplib.SMTP_SSL('smtp.163.com', 465)
            s.login(msg_from, password)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print('成功发送')
        except BaseException as e:
            print(e)


def getdata():
    global manuallist
    # 环境变量添加了的话就不用手打路径。启动driver
    driver = webdriver.edge(
        executable_path=r"C:\Program Files\Python312\Scripts\edgedriver_win64\msedgedriver.exe")
    driver.get("https://gushitong.baidu.com/foreign/global-AUDCNY")
    # 先设置个等待时间，20s加载到这个元素。指定的等待条件是找到这个元素，定位器是一个包括定位方法和定位值的元组。使用父级元素定位。
    element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-s-00030d72]//span[contains(@class,'b_price ')]"))
        )
    data = float(element.text)
    manuallist.append(data)
    judge_ifnot_del()
    sendemail(manuallist,data)
    driver.quit()
    return data


def run_schedule():
    while True:
        schedule.run_pending()  # 运行schedule模块的任务
        time.sleep(1)  # 等待1秒，避免CPU占用过高
# 创建一个单独线程thread来运行 run_schedule 函数，此时该线程会在后台一直运行，直到检测到任务。
# 如果不设置单独的线程则会导致主线程堵塞，一直循环执行schedule的任务不会回到主程序中执行后续代码即不输出数据。
schedule_thread = threading.Thread(target=run_schedule)
schedule_thread.start()
# 设定schedule模块的任务，当任务创建后并不会立刻执行，而是被添加到调度器中，因此需要写个运行调度器的函数。
schedule.every(15).minutes.do(getdata)

while True:
    print(manuallist)
    time.sleep(10)
