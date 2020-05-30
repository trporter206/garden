import csv
import pprint
import datetime
import struct
import pprint
import math
from PIL import Image


gr_values = {''         : 0,
             'Slow'     : 1,
             'Moderate' : 2,
             'Fast'     : 3
             }
e_values = {''                                 : 0,
            'Sheltered'                        : 1,
            'Deep shade'                       : 2,
            'Filtered shade'                   : 3,
            'Part sun/part shade'              : 4,
            'Full sun only if soil kept moist' : 5,
            'Full sun'                         : 6,
            }
s_values = {''                         : 0,
            'Acidic'                   : 1,
            'Alkaline'                 : 2,
            'Bog'                      : 3,
            'Humus rich'               : 4,
            'Rocky or gravelly or dry' : 5,
            'Well-drained'             : 6}
h_values = {'Zone 1: (below -46 C)'   : 1,
            'Zone 2: (-46 to -40 C)'  : 2,
            'Zone 3: (-40 to -34 C)'  : 3,
            'Zone 4: (-34 to -29 C)'  : 4,
            'Zone 5: (-29 to -23 C)'  : 5,
            'Zone 6: (-23 to -18 C)'  : 6,
            'Zone 7: (-18 to -12 C)'  : 7,
            'Zone 8a: (-12 to -9.5 C)': 8,
            'Zone 8b: (-9.4 to -7 C)' : 8,
            'Zone 9: (-7 to -1 C)'    : 9,
            'Zone 10: (-1 to 4 C)'    : 10,
            'Zone 11: (above 4 C)'    : 11}
w_values = {''           : 0,
            'NA'         : 0,
            'Low'        : 1,
            'Summer dry' : 2,
            'Moderate'   : 3,
            'High'       : 4,
            'Wetlands'   : 5,
            'Aquatic'    : 6}

def searchPlant(name):
    with open('plantList.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if row[0] == name:
                return row

def plant_facts(plant):
    plant = searchPlant(plant)
    print(f"Plant name: {plant[0]}")
    print(f"Growth rate: {plant[1]}")
    print(f"Exposure: {plant[2]}")
    print(f"Soil: {plant[3]}")
    print(f"Hardiness: {plant[4]}")
    print(f"Water use: {plant[5]}")

def minimumSizeHelper(plants):
    size_needed = 0
    if len(plants) == 0:
        return 0
    else:
        for plant in plants:
            print(plant)
            size_needed+=plants[plant].volume
    return size_needed

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = {}
        self.minimum_size = 0

    def add_plant(self, plant):
        plant_info = searchPlant(plant)
        if plant_info == None:
            print("Plant not in database")
        else:
            new_plant = Plant(plant_info[0], plant_info[1], plant_info[2],
                                                            plant_info[3],
                                                            plant_info[4],
                                                            plant_info[5],
                                                            plant_info[6],
                                                            plant_info[7],
                                                            plant_info[8],
                                                            plant_info[9],
                                                            plant_info[10])
            self.plants[plant_info[0]] = new_plant
            self.minimum_size = self.minimumSize()
            # print("Your "+plant+" was added to "+self.name)

    def remove_plant(self, plant):
        if plant in self.plants:
            p = self.plants.pop(plant)
            self.minimum_size = self.minimumSize()
            del p
            print(plant+" removed from "+self.name)
        else:
            print(plant+" not found in "+self.name)

    def list_plants(self):
        if len(self.plants) == 0:
            print("no plants in your garden!")
            return
        print("Your garden has "+str(len(self.plants))+" plants")
        for key, value in self.plants.items():
            pprint.pprint(vars(value))

    def filter_plants(self, field, search):
        filtered_plants = []
        for key, value in self.plants.items():
            print(key, value)
            if getattr(value, field) == search:
                filtered_plants.append(value.name)
        print("Found "+str(len(filtered_plants))+" plants")
        return filtered_plants

    def clear_plants(self):
        if len(self.plants) == 0:
            print("No plants to remove")
        else:
            self.plants.clear()
            self.minimum_size = self.minimumSize()

    def minimumSize(self):
        return minimumSizeHelper(self.plants)

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
        print(f'Growth Rate average (0-3): {sum(gRate_average)/len(gRate_average)}')
        print(f'Exposure average (0-5): {sum(exp_average)/len(exp_average)}')
        print(f'Soil type average (0-6): {sum(soil_average)/len(soil_average)}')
        print(f'Hardiness zone average (1-11): {sum(hard_average)/len(hard_average)}')
        print(f'Water use average (0-6): {sum(wa_average)/len(wa_average)}')
        print(f'Minimum size needed: {self.minimumSize()} square meters')


class Plant(Garden):
    def __init__(self, name, growth_rate, exposure, soil, hardiness, water,
                                                                  height,
                                                                  spread,
                                                                  colourInSummer,
                                                                  colourInFall,
                                                                  colourPetals):
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
        self.colourInSummer = colourInSummer
        self.colourInFall = colourInFall
        self.colourPetals = colourPetals
        self.plant_date = datetime.datetime.now()
        self.notes = ""
        self.pattern = Image.open("plant patterns/"+name+".jpg")

    def describe(self):
        pprint.pprint(vars(self))

    def edit_notes(self, note):
        self.notes = note

    def age(self):
        age = datetime.datetime.now() - self.plant_date
        return age

    def show_pattern(self):
        return self.pattern.show()
