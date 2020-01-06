import csv
import matplotlib.pyplot as plt
from datamanagers.datamanager import Dataset

print('''------------------------------------------------------------------------------------------------------------------------
WARNING:
Csvmanager imported as module.
For more info about, see README.md file or visit https://github.com/NicolaM94/StatisticProject.
------------------------------------------------------------------------------------------------------------------------
''')

while True:
    try:
        path = input("Enter the path of the file (something like C:/Users/Desktop/file.csv):\n")
        file = open(path)
        reader = csv.reader(file)
        header = next(reader)
        break
    except FileNotFoundError:
        print("Could not find any file named",path,"\n")

print("Variables found in the raw data:\n",header,"\nWich variables do you want me to pick? Insert the variables like 'var1,var3,var4,...'")
chosen = input()
mods = input("Do you want to specify more filters for each variable? See README.md for typing rules. If no type 'NO'\n")



