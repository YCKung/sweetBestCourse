#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
#http://140.112.161.31/NTUVoxCourse/index.php/uquery/cou?DPRNDPT=9010%20&QPYEAR=100&MSLGRD=3
user = raw_input('student id:')
grade = raw_input('grade:')

department = user[3:6]

session1 = requests.session()

url = "http://140.112.161.31/NTUVoxCourse/index.php/uquery/cou?DPRNDPT="
url += department + "0%20&QPYEAR=100&MSLGRD=" + grade

res = session1.get(url)
soup = bs(res.text)
table = soup.select("tr")
i=0 
bi_show = []
fu_shwen_bi_show = []
for row in table:
    i+=1
    if i<4:
        continue
    items = row.findAll("td")
    if not len(items) == 7:
        continue
    if items[4].text=='': 
        bi_show.append(items[1].text)
    else:
    	fu_shwen_bi_show.append(items[1].text)

print "\nbi show:"
for item in bi_show:
	print item


print "\nfu shwen bi show:"
for item in fu_shwen_bi_show:
	print item