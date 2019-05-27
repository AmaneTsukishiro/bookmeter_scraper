# This is a modification of takeBooks.py by walk_to_work https://qiita.com/walk_to_work/items/6b0f3c6de25921a11d7b
#
# Required: chromedriver.exe
#
# Get the fllowing data
#   Read: Title, Authors, Pages, Date
#   Reading: Title*, Authors
#   Stacked: Title*, Authors
#   Wish: Title*, Authors
# * Titles may be abbreviated (max length = 23)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import requests
import math
import time
from bs4 import BeautifulSoup
import csv
from datetime import datetime

usr_id = xxxxx
email = 'email address'
password = 'password'

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get('https://bookmeter.com/login/')

driver.find_element_by_id('session_email_address').send_keys(email)
driver.find_element_by_id('session_password').send_keys(password)
driver.find_element_by_name('button').click()

time.sleep(5)

def getPageNum(category):
    url = 'https://bookmeter.com/users/'+str(usr_id)+'/books/'+category
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    num = int((soup.find(class_='content__count').string))
    page = math.ceil(num/20)
    return page

nowdate = datetime.now()

for category in ['read', 'reading', 'stacked', 'wish']:
    print('getting '+category+' books')
    page = getPageNum(category)
    books = []
    for i in range(page):
        print('page '+str(i+1))
        url = 'https://bookmeter.com/users/'+str(usr_id)+'/books/'+category
        if category == 'read':
            url += '?display_type=list'
        if i != 0:
            if category == 'read':
                url += '&page='+str(i+1)
            else:
                url += '?page='+str(i+1)
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title_array = []
        author_array = []
        page_array = []
        date_array = []
        for results in soup.find_all(class_='book__detail'):
            for title in results.find_all(class_='detail__title'):
                title_array.append(str(title.string))
            for author in results.find_all(class_='detail__authors'):
                author_array.append(str(author.string)) 
            if category == 'read':
                for page in results.find_all(class_='detail__page'):
                    page_array.append(str(page.string))
                for date in results.find_all(class_='detail__date'):
                    date_array.append(str(date.string))
        for i in range(len(title_array)):
            listData = []
            listData.append(title_array[i])
            listData.append(author_array[i])
            if category == 'read':
                listData.append(page_array[i])
                listData.append(date_array[i])
            books.append(listData)
    filename = str(usr_id)+'_'+category+'_'+nowdate.strftime('%Y%m%d')+'.csv'
    print('writing ' + filename)
    f = open(filename, 'w', encoding='UTF-8', newline='')
    csvWriter = csv.writer(f)
    csvWriter.writerows(books)
    f.close()
    print('done')

