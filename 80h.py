from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


#1, 2
my_driver = webdriver.Chrome()
my_driver.get("https://www.github.com")
a = my_driver.title
print(a)
sleep(1)

my_driver.refresh()
my_driver.close()

#sleep(1)
#driver = webdriver.Firefox(executable_path=r'/usr/lib/firefox/firefox.sh')
#driver.get('http://www.ynet.co.il')
#binary = FirefoxBinary('/usr/lib/firefox')
#my_driver2 = webdriver.Firefox(firefox_binary=binary)
# 3 - Yes, the same locator
my_driver = webdriver.Chrome()
my_driver.get("https://www.bbc.com/")
a = my_driver.title
my_driver.close()

#4
my_driver_chrome = webdriver.Chrome()
my_driver_chrome.get('https://translate.google.co.il/?hl=iw')
text_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'
my_driver_chrome.find_element_by_xpath(text_xpath).send_keys('בוקר טוב עולם')
#data = my_driver_chrome.find_element_by_id('ucj-3')
sleep(1)
# print(my_driver_chrome.find_element_by_id('yDmH0d').text)
my_driver_chrome.close()

#5
my_driver_chrome = webdriver.Chrome()
my_driver_chrome.get('https://www.youtube.com/')
text_xpath = '//*[@id="search"]'
my_driver_chrome.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("Roses")
my_driver_chrome.find_element_by_id('search-icon-legacy').click()
sleep(1)
# print(my_driver_chrome.find_element_by_id('yDmH0d').text)
my_driver_chrome.close()

#6
my_driver_chrome = webdriver.Chrome()
my_driver_chrome.get('https://translate.google.co.il/?hl=iw')
sleep(1)
# print(my_driver_chrome.find_element_by_id('yDmH0d').text)
my_driver_chrome.close()


#7
my_driver_chrome = webdriver.Chrome()
my_driver_chrome.get("https://www.facebook.com/")
my_driver_chrome.find_element_by_id("email").send_keys("arik@atiya.com")
my_driver_chrome.find_element_by_id("pass").send_keys("Arikatiya1010")
my_driver_chrome.close()



