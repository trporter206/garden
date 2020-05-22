import csv
from gardens import *

# with open('plants.csv', mode='r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row[0])

garden = Garden("test garden")
garden.add_plant('Korean fir')
garden.add_plant('common aster')
garden.add_plant('beautyberry ')

print(garden.filter_plants('water','Moderate'))
