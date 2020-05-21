from plants import Plant
from gardens import Garden
from scraper import plant_names

g = Garden('mygarden')
p = Plant('tulip', 'flower', 'my favorite flower')
p1 = Plant('oak', 'tree', 'a tall tree')
g.add_plant(p)

for plant in plant_names:
    print(plant.text)
