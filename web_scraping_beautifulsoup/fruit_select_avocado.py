from bs4 import BeautifulSoup
import os
""" LESSON : Various EXTRACTION of WORD 'AVOCADO' from Web-site (p.39)
  (1) select from CSS
  (2) extract form -- find.METHOD
  (3) Use find.METHOD repeatedly!
"""

FILE_NAME = '01_fruit.html'
DESTIN_DIR = os.path.join(os.path.dirname(__file__),'sample_html', FILE_NAME)
print(DESTIN_DIR)

file_html = open(DESTIN_DIR, encoding='UTF-8')
soup = BeautifulSoup(file_html, 'html.parser')

# (1) select from CSS
print(soup.select_one('li:nth-of-type(8)').string)              # AVOCADO
print(soup.select_one('#ve-list > li:nth-of-type(4)').string)   # AVOCADO

print(soup.select("#ve-list > li[data-lo='us']")[1].string)     # AVOCADO
print(soup.select('#ve-list > li.black')[1].string)             # AVOCADO


# (2) extract form -- find.METHOD
condition_dict = {"data-lo":'us', 'class':'black'}
print(soup.find("li", condition_dict).string)                   # AVOCADO

# (3) Use find.METHOD repeatedly!
print(soup.find(id='ve-list')
          .find("li", condition_dict)
          .string)                                              # AVOCADO
