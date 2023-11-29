import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj=Service("C:/Users/konda/Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

