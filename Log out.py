from selenium import webdriver
from time import sleep
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/Logout.php')


sleep(5)
browser.quit()