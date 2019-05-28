# bookmeter_scraper
bookmeter_scraper is literally a scraper for bookmeter.com. You can get the following data (as separated csv files):
+ Information of "yonda" books: Titles, Authors, Pages, Dates you finished reading.
+ Information of "yonderu", "tsundoku" and "yomitai" books: Titles, Authors.
## Usage
Prepare [Python](https://www.python.org/).
### bookmeter_scraper.py
+ Enter your bookmeter id (which is a natural number) to the variable `usr_id` in the source file.
+ Execute the command: `$ python bookmeter_scraper.py`.
### bookmeter_scraper_chrome.py
+ Install [Chrome](https://www.google.com/intl/ja/chrome/) if you have not installed.
+ Download [chromedriver.exe](http://chromedriver.chromium.org/downloads) and put it to the same directory as the source file.
+ Enter your bookmeter id, email address and password to the variables `usr_id`, `email` and `password` resp. in the source file.
+ Execute the command: `$ python bookmeter_scraper_chrome.py`.
## Limitations
See https://github.com/yuishiyumeiji/bookmeter_scraper/issues/1.

### Acknowledgement
bookmeter_scraper is a modification of walk_to_work's [takeBooks.py](https://qiita.com/walk_to_work/items/6b0f3c6de25921a11d7b). The distribution has been permitted by xem. I appreciate xyr permission.
