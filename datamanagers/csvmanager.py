import csv
import matplotlib.pyplot as plt
from datamanagers.datamanager import Dataset


path = input("Enter the path of the file (something like C:/Users/Desktop/file.csv): ")

file = open(path)
reader = csv.reader(file)
header = next(reader)

print("Discriminating variables found in the file:",header,"Wich variables do you want me to pick? Insert the variables like 'age,name,county,...'")
chosen = input()

file.close()