from selenium import webdriver
from time import sleep
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/WithdrawalInput.php')

elem = browser.find_element_by_name("accountno")
elem.send_keys("170220")

elem = browser.find_element_by_name("ammount")
elem.send_keys("5000000")

elem = browser.find_element_by_name("desc")
elem.send_keys("money")

elem = browser.find_element_by_name("AccSubmit")
elem.click()

sleep(5)
browser.quit()