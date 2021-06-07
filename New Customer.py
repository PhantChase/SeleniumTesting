from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.alert import Alert
#mngr327677
#vuhegyv

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()
browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("huyGender")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()
browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("02202000")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()
browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("Ngu Hanh Son")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("Da Nang")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("Da Nang")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("112233")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("0915674582")

elem = browser.find_element_by_name("emailid")
elem.send_keys("")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("")

elem = browser.find_element_by_name("addr")
elem.send_keys("")

elem = browser.find_element_by_name("city")
elem.send_keys("")

elem = browser.find_element_by_name("state")
elem.send_keys("")

elem = browser.find_element_by_name("pinno")
elem.send_keys("")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("")

elem = browser.find_element_by_name("emailid")
elem.send_keys("lmhuy.18it3@vku.udn.vn")

elem = browser.find_element_by_name("password")
elem.send_keys("")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()

browser = webdriver.Edge(r"msedgedriver.exe")

browser.get('http://www.demo.guru99.com/V4/manager/addcustomerpage.php')

elem = browser.find_element_by_name("name")
elem.send_keys("Phan Tri Dung")

# elem = browser.find_element_by_name("rad1")
# elem.click()

# elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
# elem.click()

elem = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
elem.click()

elem = browser.find_element_by_name("dob")
elem.send_keys("02172000")

elem = browser.find_element_by_name("addr")
elem.send_keys("75 Duong Ton Hai")

elem = browser.find_element_by_name("city")
elem.send_keys("Da Nang")

elem = browser.find_element_by_name("state")
elem.send_keys("Da Nang")

elem = browser.find_element_by_name("pinno")
elem.send_keys("170220 ")

elem = browser.find_element_by_name("telephoneno")
elem.send_keys("0877464243")

elem = browser.find_element_by_name("emailid")
elem.send_keys("phantridungdz@gmail.com")

elem = browser.find_element_by_name("password")
elem.send_keys("dungdeptrai")

elem = browser.find_element_by_name("sub")
elem.click()

alert = Alert(browser)

print(alert.text)

alert.accept()

sleep(2)
browser.quit()