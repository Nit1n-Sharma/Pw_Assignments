import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = "http://www.electionharyanatest.rjdemo.wwhnetwork.net/WebCMS/Start/1519"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

