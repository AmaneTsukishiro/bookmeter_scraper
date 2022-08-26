# This is a modification of takeBooks.py by walk_to_work https://qiita.com/walk_to_work/items/6b0f3c6de25921a11d7b
#
# Get the fllowing data
#   Read: Title*, Authors, Pages, Date
#   Reading: Title*, Authors
#   Stacked: Title*, Authors
#   Wish: Title*, Authors
# * Titles may be abbreviated (max length = 23)

import requests
import math
import time
from bs4 import BeautifulSoup
import csv
from datetime import datetime

usr_id = xxxxx
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

session = requests.session()

def getPageNum(category):
    url = 'https://bookmeter.com/users/'+str(usr_id)+'/books/'+category
    html = session.get(url, headers=headers).text.encode('utf-8')
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
        url = 'https://bookmeter.com/users/'+str(usr_id)+'/books/'+category
        if category == 'read':
            url += '&page='+str(i+1)
        else:
            url += '?page='+str(i+1)
        time.sleep(3)
        html = session.get(url, headers=headers).text.encode('utf-8')
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
    csvWriter = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
    csvWriter.writerows(books)
    f.close()
    print('done')

