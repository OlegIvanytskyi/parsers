import requests
from bs4 import BeautifulSoup, SoupStrainer

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# use of webdriver (paste the following line into the code)
# driver = webdriver.Chrome(ChromeDriverManager().install())

import re
import json
import pathlib
import time
import codecs

import pprint
pp = pprint.PrettyPrinter(indent=4)

def write_to_file(arr, category, website):
    path = f'data/{category}/{website}/'
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    
    with codecs.open(path + 'new.txt', 'w', 'utf8') as f:
        for line in arr:
            f.write((line + '\n'))
            
    print(f'{len(arr)} lines of {category} category have been scraped from {website}\n')
    print('______________________________________________________________________________')
