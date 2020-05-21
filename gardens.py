class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):
        if plant in self.plants:
            self.plants.remove(plant)

    def list_plants(self):
        print("Your garden has "+str(len(self.plants))+" plants")
        for p in self.plants:
            print(p.name)

    def potted_plants(self):
        potted_plants
        if len(self.plants) == 0:
            return "No plants in garden!"
        else:
            for p in self.plants:
                if p.potted is True:
                    potted_plants.append(p)
        return potted_plants
