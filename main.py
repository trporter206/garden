import csv
from gardens import *

# with open('plantsNew.csv', mode='r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     values = set()
#     line = 0
#     for row in csv_reader:
#         if line == 1000: break
#         if row[1] not in values:
#             values.add(row[5])
#     print(len(values))
#     pprint.pprint(values)

with open('plantList.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line == 50: break
        pprint.pprint(row)
        line +=1

# garden = Garden("test garden")
# garden.add_plant('Korean fir')
# garden.add_plant('common aster')
# garden.add_plant('beautyberry ')
#
# garden.stats()
