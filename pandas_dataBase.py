import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

"""Задание 3. Идём на https://data.mos.ru/ (https://data.mos.ru/) скачиваем 
любой интересующий вас (и подходящий по смыслу задачи)  датасет (json,csv,xml), 
пишем код импорта по внутреннюю структуру (словарь, список), создаём sqllite3 БД,
 прогружаем туда данные (список колонок как в исходном файле). Пишем 2-3 запроса с 
 использованием агрегативных функция для вывода общей информации о датасете 
 (кол-во строк, кол-во уникальных значений в колонках и т.п.), распределение количества
  по записей по какой-либо неуникальной колонке.  Из полученных агрегированных данных строим 
  столбчатую диаграмму в матплотлибе (например для датасета про вызовы пожарных
   - распределение кол-ва вызовов по годам). 
   
   Задание 4. Всё то же самое выполняем на датасете с помощью 
   Pandas (график нарисовать можно тоже с помощью него).
   """

db = pd.read_csv("data.csv", delimiter=';', names=["ID", "AdmArea", "Year", "global_id", "Month", "Calls", "trash"])
db.drop([0,8], inplace=True)
db["Calls"] = pd.to_numeric(db["Calls"])
db=db.sort_values(by=['Calls'])

#select max(calls), area_id, area from fire_stat group by calls
print(db[["ID", "AdmArea", "Calls"]].groupby("Calls"))

#select sum(calls), month from fire_stat group_by month
print(db[["Month", "Calls"]].groupby("Month").sum())

pic=db[["Year", "Calls"]].groupby("Year").sum()
temp=pic.plot()
plt.show()

