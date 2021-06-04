from selenium import webdriver
from time import sleep
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/CustomisedStatementInput.php')

elem = browser.find_element_by_name("accountno")
elem.send_keys("170220")

elem = browser.find_element_by_name("fdate")
elem.send_keys("04/17/1996")

elem = browser.find_element_by_name("tdate")
elem.send_keys("02/17/2000")

elem = browser.find_element_by_name("amountlowerlimit")
elem.send_keys("500000")

elem = browser.find_element_by_name("numtransaction")
elem.send_keys("500000")

elem = browser.find_element_by_name("AccSubmit")
elem.click()

sleep(5)
browser.quit()