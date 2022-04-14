from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome()
my_driver.get("file:/home/arik/Downloads/4.1/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[5]").click()
my_driver.find_element_by_xpath("//*[@id=\"calculate\"]").click()
expected_tip = "2.40"
actual_tip = my_driver.find_element_by_id("tip").text
print(actual_tip)
assert expected_tip == actual_tip



