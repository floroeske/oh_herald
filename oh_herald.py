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

for each_p in soup.findAll('p'):
    i_style = each_p.get('style')
    i_class = each_p.get('class')

    if i_class is None:
        continue

    if i_class == []:
        continue

    if i_style == "display:none":
        guessed_tag = i_class[0]
        print("guessed tag:", guessed_tag)
        break

if guessed_tag == "":
    print("no tag found")
    sys.exit()

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
