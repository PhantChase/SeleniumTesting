from selenium import webdriver
from time import sleep
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("phantridungdz")

# elem = browser.find_element_by_name("rad1")
# elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("02/17/2000")

elem = browser.find_element_by_name("addr")
elem.send_keys("75 Dương Tôn Hải")

elem = browser.find_element_by_name("city")
elem.send_keys("Da Nang")

elem = browser.find_element_by_name("state")
elem.send_keys("Ngu Hanh Son")

elem = browser.find_element_by_name("pinno")
elem.send_keys("170220")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("+84377832696")

elem = browser.find_element_by_name("emailid")
elem.send_keys("phantridungdz@gmail.com")

elem = browser.find_element_by_name("password")
elem.send_keys("anhyeuem123")

elem = browser.find_element_by_name("sub")
elem.click()

sleep(5)
browser.quit()