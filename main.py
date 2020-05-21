import csv
from plants import Plant
from gardens import Garden

with open('plants.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[4])
            break
