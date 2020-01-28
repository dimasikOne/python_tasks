import requests
from bs4 import BeautifulSoup
import csv

data = []
weekday = []
temperature = []
possibility = []
wind = []

response = requests.get('https://dfedorov.spb.ru/python3/ya_forecast.html')
html = BeautifulSoup(response.content)

data = html.find_all('div', class_='forecast-label')
for i in range(len(data)):
    weekday.append(data[i].text)

data.clear()

data = html.find_all('div', class_='forecast-text')
for i in range(len(data)):
    data[i] = data[i].text

for i in range(len(data)):
    index =  data[i].find("м/с")
    wind.append(data[i][index-3:index])
    index = data[i].find("градус")
    temperature.append(data[i][index - 3: index])
    index = data[i].find("%")
    possibility.append(data[i][index - 2: index])

with open('data.csv', 'w', newline='') as csv_file:
    writer=csv.writer(csv_file, delimiter=" ")
    writer.writerow("weekday\ttemperature\twind\tpossibility")
    writer.
    for i in range(len(wind)):
        writer.writerow(weekday[i]+"\t"+temperature[i]+"\t"+wind[i]+"\t"+possibility[i])