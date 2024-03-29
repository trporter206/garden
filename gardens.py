import csv
import pprint
import datetime
import struct
import pprint
import math
from PIL import Image
import os.path
from os import path

class Garden:
    plant_values = {
        'growth_rate' : ['', 'Slow', 'Moderate', 'Fast'],
        'exposure'    : ['', 'Sheltered', 'Deep shade', 'Filtered shade',
                                                       'Part sun/part shade',
                                                        'Full sun only if soil kept moist',
                                                        'Full sun'],
        'soil'        : ['', 'Acidic', 'Alkaline', 'Bog', 'Humus rich',
                                                          'Rocky or gravelly or dry',
                                                          'Well-drained'],
        'hardiness'   : ['Zone 1: (below -46 C)', 'Zone 2: (-46 to -40 C)',
                                                  'Zone 3: (-40 to -34 C)',
                                                  'Zone 4: (-34 to -29 C)',
                                                  'Zone 5: (-29 to -23 C)',
                                                  'Zone 6: (-23 to -18 C)',
                                                  'Zone 7: (-18 to -12 C)',
                                                  'Zone 8a: (-12 to -9.5 C)',
                                                  'Zone 8b: (-9.4 to -7 C)',
                                                  'Zone 9: (-7 to -1 C)',
                                                  'Zone 10: (-1 to 4 C)',
                                                  'Zone 11: (above 4 C)'],
        'water'       : ['', 'NA', 'Low', 'Summer dry', 'Moderate', 'High', 'Wetlands', 'Aquatic']
    }

    def __init__(self):
        self.name = 'Garden'
        self.plants = {}
        self.size = 0
        self.maximumSize = 0

    @staticmethod
    def searchPlant(name):
        with open('plantList.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                if row[0] == name:
                    return row
        return None

    @staticmethod
    def plant_facts(plant):
        plant = searchPlant(plant)
        print("Plant name: {plant}".format(plant=plant[0]))
        print("Growth rate: {plant}".format(plant=plant[1]))
        print("Exposure: {plant}".format(plant=plant[2]))
        print("Soil: {plant}".format(plant=plant[3]))
        print("Hardiness: {plant}".format(plant=plant[4]))
        print("Water use: {plant}".format(plant=plant[5]))

    @classmethod
    def add_plant(self, plant, garden):
        plant_info = self.searchPlant(plant)
        if plant_info == None:
            print("Plant not in database")
            return None
        else:
            new_plant = Plant(plant_info[0], plant_info[1], plant_info[2],
                                                            plant_info[3],
                                                            plant_info[4],
                                                            plant_info[5],
                                                            plant_info[6],
                                                            plant_info[7],
                                                            plant_info[8],
                                                            plant_info[9],
                                                            plant_info[10],
                                                            plant_info[11])
            garden.plants[plant_info[0]] = new_plant
            garden.minimum_size = garden.minimumSize(garden)
            garden.size+= float(plant_info[7])
            print("add_plant successful")

    @classmethod
    def remove_plant(self, plant):
        if plant in self.plants:
            p = self.plants.pop(plant)
            self.minimum_size = self.minimumSize()
            del p
            print(plant+" removed from "+self.name)
        else:
            print(plant+" not found in "+self.name)

    @classmethod
    def list_plants(self):
        if len(self.plants) == 0:
            print("no plants in your garden!")
            return
        print("Your garden has "+str(len(self.plants))+" plants")
        return list(self.plants.keys())

    @classmethod
    def filter_plants(self, field, search):
        filtered_plants = []
        for key, value in self.plants.items():
            print(key, value)
            if getattr(value, field) == search:
                filtered_plants.append(value.name)
        print("Found "+str(len(filtered_plants))+" plants")
        return filtered_plants

    @classmethod
    def clear_plants(self):
        if len(self.plants) == 0:
            print("No plants to remove")
        else:
            self.plants.clear()
            self.minimum_size = self.minimumSize()

    @classmethod
    def minimumSize(self, garden):
        size_needed = 0
        if len(garden.plants) == 0:
            return 0
        else:
            for plant in garden.plants:
                print(plant)
                size_needed+=garden.plants[plant].volume
        return size_needed

    @classmethod
    def stats(self):
        gRate_average = []
        exp_average = []
        soil_average = []
        hard_average = []
        wa_average = []
        for value in self.plants.values():
            gRate_average.append(gr_values[value.growth_rate.split(',')[0]])
            exp_average.append(e_values[value.exposure.split(',')[0]])
            soil_average.append(s_values[value.soil.split(',')[0]])
            hard_average.append(h_values[value.hardiness.split(',')[0]])
            wa_average.append(w_values[value.water.split(',')[0]])
        print('Growth Rate average (0-3): {stat}'.format(stat=sum(gRate_average)/len(gRate_average)))
        print('Exposure average (0-5): {stat}'.format(stat=sum(exp_average)/len(exp_average)))
        print('Soil type average (0-6): {stat}'.format(stat=sum(soil_average)/len(soil_average)))
        print('Hardiness zone average (1-11): {stat}'.format(stat=sum(hard_average)/len(hard_average)))
        print('Water use average (0-6): {stat}'.format(stat=sum(wa_average)/len(wa_average)))
        print('Minimum size needed: {stat} square meters'.format(stat=self.minimumSize()))


class Plant():
    def __init__(self, name, growth_rate, exposure, soil, hardiness, water,
                                                                  height,
                                                                  spread,
                                                                  colourInSummer,
                                                                  colourInFall,
                                                                  colourPetals,
                                                                  image):
        self.name = name
        self.growth_rate = growth_rate
        self.hardiness = hardiness
        self.exposure = exposure
        self.soil = soil
        self.water = water
        if height == '':
            self.height = float(0)
        else:
            self.height = float(height)
        if spread == '':
            self.spread = float(0)
        else:
            self.spread = float(spread)
        self.volume = float(math.pi*(self.spread**2)*self.height)
        self.coverage = float(self.spread**2)
        self.colourInSummer = colourInSummer
        self.colourInFall = colourInFall
        self.colourPetals = colourPetals
        self.plant_date = datetime.datetime.now()
        self.notes = ""
        self.image = image


    def describe(self):
        pprint.pprint(vars(self))

    def edit_notes(self, note):
        self.notes = note

    def age(self):
        age = datetime.datetime.now() - self.plant_date
        return age

    def show_pattern(self):
        return self.pattern.show()
