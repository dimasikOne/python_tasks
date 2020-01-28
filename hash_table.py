import random
import datetime
from datetime import timedelta, datetime

class hash_table():
    def __def__(self,hash_key_to_set, data_to_set):
        self.data=data_to_set
        self.hash_key=hash_key_to_set

    def __init__(self):
        hkey=random.randint(1,100)
        self.hash_key = hkey
        self.data = list()
        for i in range(self.hash_key):
            self.data.append([])


    def addData(self, data):
        index=data%self.hash_key
        self.data[index].append(data)

    def printHashTable(self):
        if(len(self.data)==0):
            print("Empty table")
            return

        for i in range(self.hash_key):
            print(self.data[i])

    def findData(self, data):
        for i in self.data[data%self.hash_key]:
            if(i==data):
                print("found "+str(i)+ "!")
                return
        print("No such data")

    def deleteData(self, data):
        if(data in self.data[data % self.hash_key]== 1):
            self.data[data % self.hash_key].remove(data)
        else:
            print("No such data")

    def clearTable(self):
        self.data.clear()



times = dict()
for i in range(1,10000):
    hm = hash_table()
    all_time = datetime.now()
    for j in range(i):
        hm.addData(random.randint(1,100))
    all_time=all_time-datetime.now()
    times[i]=all_time
    hm.clearTable()
print(times)
