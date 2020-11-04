import requests
from bs4 import BeautifulSoup
import pprint
import mysql.connector

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    title1 = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                title1.append(title)
                print(title1)
    return db_connector(title1)


def db_connector(title2):
    print(title2)
    mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="company")
    dbse = mydb.cursor()
    dbse.execute("DROP TABLE IF EXISTS Webpage3")
    dbse.execute('CREATE TABLE Webpage3 (title varchar(255))')
    SQL1 = "INSERT INTO Webpage2(title) VALUES (%s)"
    val1 = [title2]
    dbse.executemany(SQL1, val1)
    mydb.commit()


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
