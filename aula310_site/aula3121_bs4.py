import re

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
# print(parsed_html.title.text)

topjobs = parsed_html.select_one('#intro > div > div > article > h2')
# if topjobs is not None:
#     # print(topjobs.parent)

article = topjobs.parent

if article is not None:
    for p in article.select('p'):
        print(re.sub(r'\s{1,}', ' ', p.text).strip())
