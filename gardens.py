import csv
import pprint
import datetime
import struct

def searchPlant(name):
    with open('plants.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if row[0] == name:
                return row

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = {}

    def add_plant(self, plant):
        plant_info = searchPlant(plant)
        if plant_info == None:
            print("Plant not in database")
        else:
            new_plant = Plant(plant_info[0],
                              plant_info[1],
                              plant_info[2],
                              plant_info[3],
                              plant_info[4],
                              plant_info[5])
            self.plants[plant_info[0]] = new_plant
            print("Your "+plant+" was added to "+self.name)

    def remove_plant(self, plant):
        if plant in self.plants:
            p = self.plants.pop(plant)
            del p
            print(plant+" removed from "+self.name)
        else:
            print(plant+" not found in "+self.name)

    def list_plants(self):
        if len(self.plants) == 0:
            print("no plants in your garden!")
            return
        print("Your garden has "+str(len(self.plants))+" plants")
        for p in self.plants:
            print(p.name)
            # pprint.pprint(vars(p))

    def filter_plants(self, field, search):
        filtered_plants = []
        for key, value in self.plants.items():
            print(key, value)
            if getattr(value, field) == search:
                filtered_plants.append(value.name)
        print("Found "+str(len(filtered_plants))+" plants")
        return filtered_plants

class Plant(Garden):

    def __init__(self, name, growth_rate, exposure, soil, hardiness, water):
        self.name = name
        self.growth_rate = growth_rate
        self.hardiness = hardiness
        self.exposure = exposure
        self.soil = soil
        self.water = water
        self.plant_date = datetime.datetime.now()
        self.notes = ""

    def describe(self):
        pprint.pprint(vars(self))

    def edit_notes(self):
        note = input('Enter new note: ')
        self.notes = note
