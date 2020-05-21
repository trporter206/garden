from plants import Plant
from gardens import Garden

g = Garden('mygarden')
p = Plant('tulip', 'flower', 'my favorite flower')
p1 = Plant('oak', 'tree', 'a tall tree')
g.add_plant(p)
print(p.plant_date)
