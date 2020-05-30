import csv
from gardens import *
import random

# with open('plantList.csv', mode='r') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     values = set()
#     attr = 6
#     firstline = True
#     for row in csv_reader:
#         if firstline:
#             firstline = False
#             continue
#         if row[attr] not in values:
#             values.add(row[attr])
#     print(len(values))
#     pprint.pprint(values)


def create_random_garden(plant_num):
    randomGarden = Garden("Random Garden")
    with open('plantList.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line = 0
        firstline = True
        for row in csv_reader:
            if firstline:
                firstline = False
                continue
            nums = random.sample(range(60), plant_num)
            if line in nums:
                randomGarden.add_plant(row[0])
                if len(randomGarden.plants) == plant_num:
                    return randomGarden
            line +=1
    return randomGarden


pprint.pprint(searchPlant('beautyberry'))
garden = create_random_garden(5)
for key, item in garden.plants.items():
    item.show_pattern()
