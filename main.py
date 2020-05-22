import csv
from gardens import *

# with open('plants.csv', mode='r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row[0])

garden = Garden("My garden")
garden.add_plant()
garden.list_plants()
garden.remove_plant()
garden.list_plants()
