import requests
from bs4 import BeautifulSoup, SoupStrainer

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import json
import pathlib
import time
import codecs

import pprint
pp = pprint.PrettyPrinter(indent=4)

def write_to_file(arr, category, website):
    num_of_articles = 0
    path = f'data/{category}/{website}/'
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    
    with codecs.open(path + 'new.txt', 'w', 'utf8') as f:
        for elem in arr:
            f.write((elem[0] + '\n' + elem[1] + '\n'))
            num_of_articles += 1
    print(f'{num_of_articles} articles of {category} category scraped from {website}\n')
