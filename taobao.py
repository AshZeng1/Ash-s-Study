from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import datetime

driver = webdriver.Edge()

#Login
def login():
    driver.get('https://www.taobao.com/')
    time.sleep(2)

    #Action chain
    actions = ActionChains(driver)
    if driver.find_element_by_link_text('亲，请登录'): 
        loginHerf = driver.find_element_by_link_text('亲，请登录')
        actions.move_to_element(loginHerf)
        actions.click(loginHerf)
        # print(loginHerf)
        actions.perform()

    print('能给老子快点登录吗？1s之内完成')
    time.sleep(15)
    # print('Sleep done')
    driver.get('https://cart.taobao.com/')
    time.sleep(2)
    # print('Sleep done')

    if driver.find_element_by_id('J_SelectAll1'):
        driver.find_element_by_id('J_SelectAll1').click()

    time.sleep(1)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(buyTime):
    while True:
        now = now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(buyTime)
        # print(now)

        if now > buyTime:
            try:
                if driver.find_element_by_id('J_Go'):
                    driver.find_element_by_id('J_Go').click()
                    driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)

times = input('给爷输抢购时间：')
time.sleep(20)
print('Sleep done')

login()
buy(times)


