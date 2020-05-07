from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://trivago.com/')
browser.forward()
browser.back()

