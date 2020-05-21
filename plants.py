import datetime

class Plant:

    def __init__(self, name, growth_rate, hardiness, exposure, soil, water):
        self.name = name
        self.growth_rate = growth_rate
        self.hardiness = hardiness
        self.exposure = exposure
        self.soil = soil
        self.water = water
        self.plant_date = datetime.datetime.now()

    def describe_self(self):
        print(self.name)
        print(self.type)
        print(self.description)

    def edit_name(self):
        name = input('Enter new name: ')
        self.name = name

    def edit_description(self):
        description = input('Enter new description: ')
        self.description = description
