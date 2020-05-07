from selenium import webdriver
#b

from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://trivago.com/')
browser.forward()
browser.back()

