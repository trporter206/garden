import datetime

class Plant:

    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description
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
