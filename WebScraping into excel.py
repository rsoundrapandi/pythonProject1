from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import pytest

r = requests.get('http://weblisting.freetemplatespot.com/testing-ground.scraping.pro').content
soup = BeautifulSoup(r, "html.parser")
body = soup.find('body')
test = body.find_all({'div', 'span', 'p', 'tr', 'td'})
res = []
for i in test:
    x = i.get('class')
    if x != None:
        res.append(x)
        print(res)
res1=tuple(res)
res2 = [''.join(i) for i in res1]
print(res2)


# df=pd.DataFrame(res)
# df.to_excel("test2.xlsx",sheet_name='Class', index=False)
