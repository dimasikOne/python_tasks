import requests
from bs4 import BeautifulSoup
from natasha import NamesExtractor
import matplotlib.pyplot as plt

data = []
titles = []
dic = {}

extractor = NamesExtractor()
r = requests.get('https://yandex.ru/news/export')
html = BeautifulSoup(r.content, "html.parser")
data = html.find_all('a', class_="link link_theme_normal i-bem")
for i in range(len(data)):
    data[i] = str(data[i])
    index1 = data[i].find("href", 0, len(data[i]))
    index2 = data[i].find("rss", 0, len(data[i]))
    r = requests.get(data[i][index1 + 6:index2 + 3])
    data[i] = BeautifulSoup(r.content, "html.parser")
    data[i] = str(data[i].findAll('title'))
    titles.append(extractor(data[i]))
    for match in titles[i]:
        start, stop = match.span
        if (dic.get(data[i][start:stop], -1) == -1):
            dic[data[i][start:stop]] = 1
        else:
            dic[data[i][start:stop]] += 1
gis = plt.subplot()
gis.bar(dic.keys(), dic.values())
plt.show()
