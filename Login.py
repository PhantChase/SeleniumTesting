from selenium import webdriver
from time import sleep
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4')

elem = browser.find_element_by_name("uid")
elem.send_keys("mngr327677")

elem = browser.find_element_by_name("password")
elem.send_keys("vuhegyv")

elem = browser.find_element_by_name("btnLogin")
elem.click()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4')

elem = browser.find_element_by_name("uid")
elem.send_keys("wrong_username")

elem = browser.find_element_by_name("password")
elem.send_keys("vuhegyv")

elem = browser.find_element_by_name("btnLogin")
elem.click()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4')

elem = browser.find_element_by_name("uid")
elem.send_keys("mngr327677")

elem = browser.find_element_by_name("password")
elem.send_keys("wrong_password")

elem = browser.find_element_by_name("btnLogin")
elem.click()

sleep(2)
browser.quit()


browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4')

elem = browser.find_element_by_name("uid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("btnLogin")
elem.click()

sleep(2)
browser.quit()

