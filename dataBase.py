import csv

with open("data.csv") as f_obj:
    reader = csv.DictReader(f_obj, delimiter=' ')
    for line in reader:
        print(line)
        