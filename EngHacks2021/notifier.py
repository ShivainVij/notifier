# import urllib, re, os, random
# import urllib.request
from bs4 import BeautifulSoup
# import xlsxwriter
# import pandas as pd
# from plyer import notification
# from openpyxl import Workbook, load_workbook
# import requests
# import webbrowser
# import cookiejar
# import _thread
# from PIL import Image
# import imagehash

# from urllib.request import Request, urlopen
# import hashlib
# from selenium import webdriver
# import time


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

import requests

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)


# options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument('--user-data-dir=/Users/shivainvij/Documents/EngHacks2021')
# options.add_argument("--profile-directory=Profile 1")
# # options.add_argument("--disable-infobars")


# options.headless = True
# driver = webdriver.Chrome(options=options)
# driver.get("https://")
# driver.save_screenshot("/Users/shivainvij/Documents/EngHacks2021/imageVerify.png")


def ScrapeLoginInitialize(link, driver):
    driver.get(link)
    input("Click enter once you have logged in! Please leave the Chrome window open if you would like to continue receiving notifications.")

def ScrapeHashLoggedIn(link, driver):
    driver.minimize_window()
    driver.get(link)
    driver.minimize_window()
    time.sleep(10)
    driver.save_screenshot("imageVerify.png")
    return str(imagehash.average_hash(Image.open("imageVerify.png")))

# def ScrapeHash(link):

#     f1 = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
#     f = urlopen(f1)
#     html = f.read()
#     f.close()

#     soup_page = soup(html, "html.parser")
#     driver.save_screenshot("Documents/EngHacks2021/"+(link + ".png"))

def DeleteIndikayt():
    os.system('clear')
    wb = load_workbook('Documents/EngHacks2021/notifs.xlsx')
    sheet = wb['Sheet1']
    i = 1
    for row in sheet.rows:
        print(str(i) + ". " + str(row[0].value))
        i += 1
    rowEdit = int(input("Indicate the number of the link you would like to stop monitoring: "))
    ws = wb.active
    ws.delete_rows(idx=rowEdit, amount=1)
    wb.save("Documents/EngHacks2021/notifs.xlsx")
    

def CreateIndikayt(driver):
    link = input("Link that you would like to monitor for changes: ")
    login = input("Is a password required for login? (Y/N) ")
    if login == "Y":

        wb = load_workbook('Documents/EngHacks2021/notifs.xlsx')
        ws = wb.active
        maxRow = ws.max_row
        ScrapeLoginInitialize(link, driver)
        ws.cell(row=(maxRow+1), column=1, value=link)
        ws.cell(row=(maxRow+1), column=2, value=ScrapeHashLoggedIn(link, driver))
        
        wb.save("Documents/EngHacks2021/notifs.xlsx")
        
    elif login == "N": 
        wb = load_workbook('Documents/EngHacks2021/notifs.xlsx')
        ws = wb.active
        maxRow = ws.max_row
        ws.cell(row=(maxRow+1), column=1, value=link)
        ws.cell(row=(maxRow+1), column=2, value=ScrapeHashLoggedIn(link, driver))
        wb.save("Documents/EngHacks2021/notifs.xlsx")

def notifyUser(site):
    notification.notify(
            #title of the notification,
            title = "New update!",
            #the body of the notification
            message = "Check " + str(site) + " for updates", 
        )

def monitor(driver):
    while True:
        wb = load_workbook('Documents/EngHacks2021/notifs.xlsx')
        sheet = wb['Sheet1']
        ws = wb.active
        i=1
        for row in sheet.rows:
            if str(row[1].value) != str(ScrapeHashLoggedIn(str(row[0].value), driver)):
                print(str(row[1].value))
                print("\n")
                print(str(ScrapeHashLoggedIn(str(row[0].value), driver)))
                #Update value
                ws.cell(row=i, column=2, value=ScrapeHashLoggedIn(str(row[0].value), driver))
                notifyUser(row[0].value)
            i += 1
        wb.save("Documents/EngHacks2021/notifs.xlsx")


#Main program starts here

# _thread.start_new_thread(monitor, (driver, ))

# while True:
#     os.system('clear')

#     print("Welcome to indikayt. Please choose one of the following options: \n")

#     print("1. Delete old indikaytor\n")
#     print("2. Create new indikaytor\n")

#     i = input("Option (1 or 2): ")

#     if i not in ['1', '2']:
#         print("Oh no! That's not an option! Press Enter to Continue")
#         input()
#     else:
#         if i == '1':
#             DeleteIndikayt()
#         else:
#             CreateIndikayt(driver)

