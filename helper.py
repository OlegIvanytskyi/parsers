import requests
from bs4 import BeautifulSoup, SoupStrainer

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# use of webdriver
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
        for elem in arr:  # elem - contains teaser_headline and teaser itself
            f.write((elem[0] + '\n' + elem[1] + '\n'))
            
    print(f'{len(arr)} articles of {category} category have been scraped from {website}\n')
    print('______________________________________________________________________________')
