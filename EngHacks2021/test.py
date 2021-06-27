import urllib, re, os, random
# import urllib.request
from bs4 import BeautifulSoup as soup
# import xlsxwriter
# import pandas as pd
from plyer import notification
from openpyxl import Workbook, load_workbook
# import requests
# import webbrowser
# import cookiejar
import _thread
# from PIL import Image
# import imagehash
from urllib.request import Request, urlopen
import hashlib
# from selenium import webdriver
# import time
from playwright.sync_api import sync_playwright
import pixelmatch
from filelock import Timeout, FileLock




# import pickle
# from selenium import webdriver

# chromeOptions = webdriver.ChromeOptions()

# driver = webdriver.Chrome(options=chromeOptions)
# driver.get("http://mail.google.com")
# input()
# pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
# driver.quit

# print("completed getting cookies")
# chromeOptions.headless = True
# driver = webdriver.Chrome(options=chromeOptions)
# driver.get("http://mail.google.com")
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     print(cookie)
#     driver.add_cookie(cookie)

# input()
# driver.save_screenshot("/Users/shivainvij/Documents/EngHacks2021/imageVerify.png")

# 




# options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument('--user-data-dir=/Users/shivainvij/Documents/EngHacks2021')
# options.add_argument("--profile-directory=Profile 1")
# # options.add_argument("--disable-infobars")


# options.headless = True
# driver = webdriver.Chrome(options=options)
# driver.get("https://")
# driver.save_screenshot("/Users/shivainvij/Documents/EngHacks2021/imageVerify.png")


# def ScrapeLoginInitialize(link, driver):
#     driver.get(link)
#     input("Click enter once you have logged in! Please leave the Chrome window open if you would like to continue receiving notifications.")

# def ScrapeHashLoggedIn(link, driver):
#     driver.minimize_window()
#     driver.get(link)
#     driver.minimize_window()
#     time.sleep(10)
#     driver.save_screenshot("imageVerify.png")
#     return str(imagehash.average_hash(Image.open("imageVerify.png")))

import calendar
import time

import math, operator

from PIL import ImageChops, Image
from functools import reduce


def rmsdiff(im1, im2):

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

print(rmsdiff(Image.open("/Users/shivainvij/Documents/EngHacks2021/1624787856.png"), Image.open("/Users/shivainvij/Documents/EngHacks2021/16247919579288.png")))
