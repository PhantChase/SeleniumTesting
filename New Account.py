from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from time import sleep
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addAccount.php')

elem = browser.find_element_by_name("cusid")
elem.send_keys("170220")
sleep(1)
select = Select(browser.find_element_by_name('selaccount'))
select.select_by_visible_text('Savings')
sleep(1)
#select.select_by_value('Savings')
elem = browser.find_element_by_name("inideposit")
elem.send_keys("19216845")
sleep(1)
elem = browser.find_element_by_name("button2")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addAccount.php')

elem = browser.find_element_by_name("cusid")
elem.send_keys("")
sleep(1)
select = Select(browser.find_element_by_name('selaccount'))
select.select_by_visible_text('Current')
sleep(1)
#select.select_by_value('Savings')
elem = browser.find_element_by_name("inideposit")
elem.send_keys("19216845")
sleep(1)
elem = browser.find_element_by_name("button2")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addAccount.php')

elem = browser.find_element_by_name("cusid")
elem.send_keys("170220")
sleep(1)
select = Select(browser.find_element_by_name('selaccount'))
select.select_by_visible_text('Current')
sleep(1)
#select.select_by_value('Savings')
elem = browser.find_element_by_name("inideposit")
elem.send_keys("19216845")
sleep(1)
elem = browser.find_element_by_name("button2")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()