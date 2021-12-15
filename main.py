
import pyautogui as pag
from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('https://bit.ly/2X2GHKW')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
time.sleep(2)

from acc import un,pw

driver.find_element_by_id('identifierId').send_keys(un)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)

driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(2)
driver.get('https://classroom.google.com')
time.sleep(8)

driver.find_element_by_xpath("""//*[@id="yDmH0d"]/div[2]/div/div[1]/div/ol/li[1]/div[1]/div[3]/h2/a[1]""").click()
time.sleep(8)
driver.find_element_by_xpath("""/html/body/div[2]/div[2]/div[2]/main/section/div/div[2]/div/div[1]/div/div[3]/div/div/span""").click()
time.sleep(5)
names=driver.find_elements_by_class_name('WkZsyc')
codes=driver.find_elements_by_class_name('NjE5zd')

t_name=[ ]
for name in names:
    z1=name.text
    z1=z1[:z1.find('\n')]
    t_name.append(z1)
names=t_name

t_code=[ ]
for code in codes:
    z2=code.text
    t_code.append(z2)
codes=t_code
report=[ ]
driver.get('https://www.onlinegdb.com/online_python_compiler')
time.sleep(10)
pag.click(x=344, y=579)
for code in codes:
    
    pag.click(x=344, y=579)
    pag.hotkey('ctrl', 'a')
    pag.press('backspace')
    pag.typewrite(code)
    pag.click(x=390, y=124)
    time.sleep(10)
    pag.click(x=353, y=622)
    
    pag.doubleClick(x=344, y=579)
    pag.click(x=344, y=579)
    time.sleep(2)
    pag.click(x=344, y=579)
    pag.hotkey('ctrl', 'a')
    pag.press('backspace')
    x=Tk().clipboard_get()
    if x=='hello python\n\n\n':
        report.append('Correct')
    else:
        report.append('Incorrect')
driver.quit()
for i in range(len(codes)):
    print('----------------------------------------------------------------------------------')
    print('                           ',names[i])
    print(codes[i],end='\n\n\n')
    print('output=',report[i])
