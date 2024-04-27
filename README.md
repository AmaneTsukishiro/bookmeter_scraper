# bookmeter_scraper
bookmeter_scraper is literally a scraper for bookmeter.com.

## Functions
### bookmeter_scraper.py
You can get the following information:
+ Read (読んだ): Abbreviated Title[^1], Authors, Pages, Read Date
+ Reading (読んでる)/Stacked (積読)/Wish (読みたい): Abbreviated Title[^1], Authors

[^1]: Book titles are abbreviated if the lengths exceed 23.

### bookmeter_scraper_chrome.py
You can get the following information:
+ Read (読んだ): Book ID, Title, Authors[^2], Pages[^2], Read Date, \[Data Modal\] (optional)
+ Reading (読んでる)/Stacked (積読)/Wish (読みたい): Book ID, Title, Authors, Pages
+ All Categories: \[Book Image\] (optional)

[^2]: If those data are changed manually, the changed data are retrieved.

This version attempts to retrieve as much information as possible.
It takes more time to retrieve information from Reading, Stacked and Wish.

## Usage
bookmeter_scraper requires [Python](https://www.python.org/) with [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) and [Requests](https://pypi.org/project/requests/).
+ `pip install beautifulsoup4`
+ `pip install requests`

### bookmeter_scraper.py
+ Edit the source file: set your bookmeter id number to the variable `usr_id`.
+ `$ python bookmeter_scraper.py`.

### bookmeter_scraper_chrome.py
bookmeter_scraper_chrome.py also requires [Chrome](https://www.google.com/intl/ja/chrome/) browser and [selenium](https://pypi.org/project/selenium/) package.
+ `pip install selenium`
+ Install Chrome if you have not installed.
+ Download [chromedriver.exe](http://chromedriver.chromium.org/downloads) and put it in the same directory as the source file.

+ Edit the source file
  + Set your bookmeter user info (required)
    + `user_id`: bookmeter ID number
    + `email`: registered email address
    + `password`: bookmeter password
  + Set the options (optional)
    + `get_read_books`: default value = True
    + `get_reading_books`: default value = True
    + `get_stacked_books`: default value = True
    + `get_wish_books`: default value = True
    + `get_data_modal`: default value = False
    + `get_cover_images`: default value = False
+ `$ python bookmeter_scraper_chrome.py`.

## Warning
Do not use it very frequently (or do adjust sleep time manually) to avoid overloading the server.

## Acknowledgement
The lite version bookmeter_scraper.py is a modification of walk_to_work's [takeBooks.py](https://qiita.com/walk_to_work/items/6b0f3c6de25921a11d7b) and distributed with permission of the original author.

----------------------------------------------------------------

Copyright (C) 2019-2024 Amane Tsukishiro
