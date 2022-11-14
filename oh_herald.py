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


# search p
for each_p in soup.findAll('p'):
    # print(type(each_div))
    # print(each_div)
    i_style = each_p.get('style')
    i_class = each_p.get('class')
    #print(i_style)
    #print(i_class)

    if i_class is None:
        continue

    if i_class == []:
        continue

    if i_style == "display:none":
        # print(i_style)
        # print(i_class) 
        guessed_tag = i_class[0]
        print("guessed tag:", guessed_tag)
        # sys.exit()
        break


# search div
# soup_divs = soup.find_all('div')
# for soup_div in soup_divs:
#     soup_class = soup_div.get('class')

#     if soup_class is None:
#         continue

#     print(soup_class)
    
#     # Maybe this works?
#     # otherwise regex for random characters
#     # ['article-media', 'AwwhiJFvQSS']
#     if len(soup_class) == 2:
#         if soup_class[0] == 'article-media':
#             guessed_tag = soup_class[1]
#             print("guessed tag:", guessed_tag)
#             # sys.exit()
#             break





# old method

    # for i in soup_class:
    #     if re.fullmatch(r'[A-Za-z]{12,}', i):
    #         guessed_tag = i
    #         print("this is guessed_tag")
    #         print(guessed_tag)
    #         sys.exit()

    # print(type(i))
    # title_search = re.search('<class=(.*)', i, re.IGNORECASE)

    # if title_search:            
    #     title = title_search.group(1)
    #     print(title)

# sys.exit()

# for tag in tags:
#     for i in soup.find_all(tag):
#         if i.has_attr("class"):
#             if len(i['class']) != 0:
#                 class_list.add(" ".join(i['class']))

# for i in class_list:
#     if re.fullmatch(r'[A-Za-z]{12,}', i):
#         guessed_tag = i

#guessed_tag = "AwwhiJFvQSS"

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
