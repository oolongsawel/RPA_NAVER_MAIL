from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip
pyautogui.PAUSE = 2  #단계마다 2초씩 텀


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://nid.naver.com/')

#ID
pyperclip.copy('yourID') #ID입력
pyautogui.hotkey('ctrl', 'v') 

#PW
pyautogui.press('tab')
pyperclip.copy('yourPassword') #비밀번호입력
pyautogui.hotkey('ctrl', 'v') 

#login button click
#time.sleep(2)
#browser.find_element_by_class_name('btn_global').click()
pyautogui.press('enter')

#mail button click
browser.get('https://nid.naver.com/user2/help/myInfo.nhn?lang=ko_KR')
browser.find_element_by_class_name('gnb_mail').click()

#to me button click (내게쓰기)
browser.get('https://mail.naver.com/')
xpath = '//*[@id="nav_snb"]/div[1]/a[2]'
browser.find_element_by_xpath(xpath).click()

#write subject
time.sleep(2)
#subject = browser.find_element_by_id('subject')
#subject.send_keys("hello world")
#browser.find_element_by_id('subject').click()
pyperclip.copy('hello world')
pyautogui.hotkey('ctrl', 'v') 



#write content (내용쓰기) ???????
time.sleep(2)
#pyautogui.press('enter')
#time.sleep(2)
pyautogui.press('tap')
#pyautogui.press('tap')
#browser.find_element_by_class_name('se2_inputarea').click()
#time.sleep(2)
#xpath2 = '//*[@id="smart_editor2_content"]/a'
#pyperclip.copy('content is...')
#pyautogui.hotkey('ctrl', 'v') 
#browser.find_element_by_xpath(xpath2).click()
#browser.find_element_by_xpath(xpath2).send_keys("content is...")



#send btn click (보내기)
browser.find_element_by_id('sendBtn').click()

# Wait for 2 seconds
time.sleep(2)

