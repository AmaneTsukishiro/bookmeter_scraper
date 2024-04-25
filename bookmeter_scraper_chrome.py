#
# (C) 2019-2024 Amane Tsukishiro
#
# You can get the fllowing information:
#   Read:
#     Book ID, Title, Authors*, Pages*, Read Date, [Data Modal]**
#   Reading/Stacked/Wish:
#     Book ID, Title, Authors, Pages
#   All Categories:
#     [book image]**
#
# *  If those data are changed manually, the changed data are retrieved.
# ** Optional (default = False)

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
import os

# User Information
user_id = '012345'
email = 'example@example.com'
password = 'password'

# Options
get_read_books = True
get_reading_books = True
get_stacked_books = True
get_wish_books = True
get_data_modal = False
get_cover_images = False

# Program Body
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get('https://bookmeter.com/login/')

driver.find_element_by_id('session_email_address').send_keys(email)
driver.find_element_by_id('session_password').send_keys(password)
driver.find_element_by_name('button').click()

time.sleep(5)
nowdate = datetime.now()

target_categories = []
if get_read_books:
    target_categories.append('read')
if get_reading_books:
    target_categories.append('reading')
if get_stacked_books:
    target_categories.append('stacked')
if get_wish_books:
    target_categories.append('wish')

def get_page_num(id, category):
    url = 'https://bookmeter.com/users/'+id+'/books/'+category
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    num = int((soup.find(class_='content__count').string))
    page = math.ceil(num/20)
    return page

def get_image(book_id, category, image_url):
    if image_url != "https://bookmeter.com/images/common/book.png":
        directory = './cover_images/' + category + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        extension = os.path.splitext(image_url)[1]
        filename = book_id.replace('/books/', 'book_image_') + extension
        save_path = directory + filename
        response = requests.get(image_url)
        with open(save_path, 'wb') as f:
            f.write(response.content)

for category in target_categories:
    print('getting '+category+' books')
    page = get_page_num(user_id, category)
    book_list = []
    header = []
    header.append("book_id")
    header.append("title")
    header.append("author")
    header.append("page")
    if category == 'read':
        header.append('date')
        if get_data_modal:
            header.append('modal')
    book_list.append(header)
    for i in range(page):
        print('page '+str(i+1))
        url = 'https://bookmeter.com/users/'+user_id+'/books/'+category
        if category == 'read':
            url += '?display_type=list'
        if i != 0:
            if category == 'read':
                url += '&page='+str(i+1)
            else:
                url += '?page='+str(i+1)
        # load book list
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        if category == 'read':
            for results in soup.find_all(class_='book__detail'):
                book_id = results.find(class_='detail__title').a.get('href')
                title = results.find(class_='detail__title').text
                authors = results.find(class_='detail__authors').text
                page = results.find(class_='detail__page').text
                date = results.find(class_='detail__date').text
                entry = [book_id, title, authors, page, date]
                if get_data_modal:
                    modal = results.find(class_='js-modal-button modal-button').get('data-modal')
                    entry.append(modal)
                # print(entry)
                book_list.append(entry)
            if get_cover_images:
                for results in soup.find_all(class_='thumbnail__cover'):
                    book_id = results.a.get('href')
                    image_url = results.a.img.get('src')
                    get_image(book_id, category, image_url)   
        else:
            for book in soup.select('div.detail__title'):
                book_id = book.a.get('href')
                book_url = 'https://bookmeter.com' + book_id
                driver.get(book_url)
                time.sleep(2)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.find(class_='inner__title').text
                authors = soup.find(class_='header__authors').text
                page = soup.find_all(class_='bm-details-side__item')[-1].text
                entry = [book_id, title, authors, page]
                # print(entry)
                book_list.append(entry)
                if get_cover_images:
                    image_url = soup.select_one('div.group__image').img['src']
                    get_image(book_id, category, image_url)            
    filename = user_id + '_' + nowdate.strftime('%Y%m%d') + '_' + category + '.csv'
    print('writing ' + filename)
    with open(filename, 'w', encoding='UTF-8', newline='') as f:
        csvWriter = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
        csvWriter.writerows(book_list)
    print('done')

