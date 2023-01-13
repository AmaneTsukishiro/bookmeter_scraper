# bookmeter_scraper
bookmeter_scraper is literally a scraper for bookmeter.com. You can get the following data (as separated csv files):
+ Information of 'yonda' books: Titles, Authors, Pages, Dates you finished reading.
+ Information of 'yonderu', 'tsundoku' and 'yomitai' books: Titles, Authors.
## Usage
bookmeter_scraper requires [Python](https://www.python.org/) with [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) and [Requests](https://pypi.org/project/requests/).
+ `pip install beautifulsoup4`
+ `pip install requests`

### bookmeter_scraper.py
+ Edit the source file: assign your bookmeter id (which is a natural number) to the variable `usr_id`.
+ `$ python bookmeter_scraper.py`.

### bookmeter_scraper_chrome.py
bookmeter_scraper_chrome.py also requires [Chrome](https://www.google.com/intl/ja/chrome/) browser and [selenium](https://pypi.org/project/selenium/) package.
+ `pip install selenium'
+ Install Chrome if you have not installed.
+ Download [chromedriver.exe](http://chromedriver.chromium.org/downloads) and put it in the same directory as the source file.

+ Edit the source file: assign your bookmeter id, registered email address and bookmeter password to the variables `usr_id`, `email` and `password`, respectively.
+ `$ python bookmeter_scraper_chrome.py`.
## Limitations
See https://github.com/yuishiyumeiji/bookmeter_scraper/issues/1.

### Acknowledgement
bookmeter_scraper is a modification of walk_to_work's [takeBooks.py](https://qiita.com/walk_to_work/items/6b0f3c6de25921a11d7b). The distribution has been permitted by xem. I appreciate xyr permission.

----------------------------------------------------------------

Copyright (C) 2019-2022 Amane Tsukishiro
