
import time
import math
import os
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  #
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )



button1 = browser.find_element_by_id('book')
button1.click()

number=browser.find_element_by_id('input_value')
x=number.text
print(x)
formula_result=calc(x)
field=browser.find_element_by_id('answer')
field.send_keys(formula_result)

button_23 = browser.find_element_by_id('solve')
button_23.click()

#



# После выполнения всех действий мы не должны забыть закрыть окно браузера

