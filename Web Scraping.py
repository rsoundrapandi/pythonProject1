import requests
import mysql.connector
from bs4 import BeautifulSoup

# import pprint

# # from numpy.core.defchararray import title
# from numpy.core.defchararray import title


url = 'https://news.ycombinator.com/'
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="Company")
dbse = mydb.cursor()
dbse.execute("DROP TABLE IF EXISTS Webpage")
dbse.execute('CREATE TABLE Webpage (title VARCHAR(255), href VARCHAR(255))')

def havekrnews(links,votes):
    hn=[]
    for inx, item in enumerate(links):
        title1 = links[inx].getText()
        href1 = links[inx].get('href', None)
        hn.append({'title':title1,'href':href1}
        if True:
            SQL1 = "insert into Webpage(title,href) VALUES (%s,%s)"
            val1 = [(title1, href1)]
            dbse.executemany(SQL1, val1)
            mydb.commit()

    return hn
# print('\nExercise 3: Scrape the website and store the data in DB')
# import requests
# from bs4 import BeautifulSoup
# import pprint
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="12345",
#   database='company'
# )
#
# dbse = mydb.cursor()
# dbse.execute('DROP TABLE IF EXISTS Website')
# dbse.execute('CREATE TABLE Website (Link VARCHAR(255), Title VARCHAR(255), Votes VARCHAR(255))')
#
# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
#
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')
# links2 = soup2.select('.storylink')
# subtext2 = soup2.select('.subtext')
#
# mega_links = links + links2
# mega_subtext = subtext + subtext2
#
# def sort_stories_by_votes(hnlist):
#     return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#                 sql = "INSERT INTO Website (Link, Title, Votes) VALUES (%s, %s, %s)"
#                 val = [(title, href, points)]
#                 dbse.executemany(sql,val)
#                 mydb.commit()
#     return sort_stories_by_votes(hn)
#
# pprint.pprint(create_custom_hn(mega_links, mega_subtext))
#
# dbse.execute('SELECT * FROM Website')
# myresult = dbse.fetchall()
# for x in myresult:
#     print(x)