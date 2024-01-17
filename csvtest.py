# import undetected_chromedriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import time
chrome_driver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
# options.headless = False
profile = "C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options)
# service = Service(executable_path=chrome_driver_path)
#
# driver = webdriver.Chrome(service=service)

driver.get("https://pypi.org/project/undetected-chromedriver/")
time.sleep(10)