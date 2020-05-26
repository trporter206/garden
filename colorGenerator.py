import csv
import pprint

summerIdentifiers = set()
fallIdentifiers = set()
petalIdentifiers = set()
def identifiers(lists):
    item = 0
    for l in lists:
        for colors in l:
            identifiers = colors.split(',')
            for i in identifiers:
                if item == 0:
                    summerIdentifiers.add(i)
                elif item == 1:
                    fallIdentifiers.add(i)
                elif item == 2:
                    petalIdentifiers.add(i)
        item+=1

def database_color_lists():
    fallList = set()
    summerList = set()
    petalsList = set()
    with open('plantList.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        values = set()
        summer = 8
        fall = 9
        petal = 10
        for row in csv_reader:
            summerList.add(row[summer])
            fallList.add(row[fall])
            petalsList.add(row[petal])
    identifiers([summerList, fallList, petalsList])

database_color_lists()
pprint.pprint(summerIdentifiers)
