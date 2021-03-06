from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
	
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
	
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector("#solve")
    button.click()
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()