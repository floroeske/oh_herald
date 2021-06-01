#!/usr/bin/env python3

import requests
import re
import sys
from bs4 import BeautifulSoup


if len(sys.argv) < 2:
    print("Usage: ./oh_herald.py [url]")
    sys.exit()

guessed_tag = ""
url = sys.argv[1]
class_list = set()
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tags = {tag.name for tag in soup.find_all()}
content = None

for tag in tags:
    for i in soup.find_all(tag):
        if i.has_attr("class"):
            if len(i['class']) != 0:
                class_list.add(" ".join(i['class']))

for i in class_list:
    if re.fullmatch(r'[A-Za-z]{12,}', i):
        guessed_tag = i

for items in soup.select("." + guessed_tag):
    tag_items = [item.text for item in items.find_previous_siblings() if item.name == "p"]
    content = tag_items

if content:
    content.reverse()
    for i in range(len(content)):
        line = content[i].replace("\n", "")
        print(line)
        if i < len(content) - 1:
            print()
