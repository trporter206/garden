import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from gardens import *
from main import *

num_plants = 15
start_garden = create_random_garden(0)

borderEffects = {
    "flat"   : tk.FLAT,
    "sunken" : tk.SUNKEN,
    "raised" : tk.RAISED,
    "groove" : tk.GROOVE,
    "ridge"  : tk.RIDGE,
}

plant_features = [
    'growth_rate',
    'exposure',
    'soil',
    'hardiness',
    'water',
    'height',
    'spread',
    'colourInSummer',
    'colourInFall',
    'colourPetals'
]

window = tk.Tk()
window.title("Gardener")
window.rowconfigure([0,1], minsize=500, weight=1)
window.columnconfigure([0,1], minsize=500, weight=1)

# methods-----------------------------------------------------------------------
def plantTextFormat(text):
    for w in frm_info.pack_slaves():
        w.pack_forget()
    for i, val in enumerate(text[1:]):
        if val == '':
            val = 'NA'
        label = tk.Label(frm_info, text=str(plant_features[i])+': '+str(val))
        label.pack()

def show_data(*args):
    index = lst_plants.curselection()
    plant_data = searchPlant(lst_plants.get(index[0]))
    plantTextFormat(plant_data)

def newGarden(count, size, max, feature):
    newGarden = create_random_garden(count)
    lst_plants.delete(0,tk.END)
    for key, value in newGarden.plants.items():
        lst_plants.insert(tk.END, key)

def addPlant_helper(plant):
    newPlant = searchPlant(plant)
    if newPlant == None:
        return None
    else:
        lst_plants.insert(tk.END, newPlant[0])
        return True

def addPlant(plant, *args):
    newPlant = addPlant_helper(plant)
    if newPlant == None:
        lbl_add['text'] = f'{plant} not in database'
    else:
        lbl_add['text'] = f'{plant} added to garden'

def use_maxplants(*args):
    pass

def removePlant(plant, *args):
    print(plant)
# widgets/frames----------------------------------------------------------------

n = Notebook(window)

frm_add = tk.Frame(n)
lbl_plantName = tk.Label(frm_add, text='Enter plant name: ')
ent_plant = tk.Entry(frm_add, width=30)
btn_addPlant = tk.Button(frm_add,
                         text='Add plant',
                         command= lambda: addPlant(ent_plant.get()))
lbl_add = tk.Label(frm_add)
lbl_plantName.pack()
ent_plant.pack()
btn_addPlant.pack()
lbl_add.pack()

frm_create = tk.Frame(n)
maxPlants = tk.StringVar(frm_create)
maxPlants.set("False")
lbl_count = tk.Label(frm_create, text='How many plants?')
ent_count = tk.Entry(frm_create, width=15)
lbl_size = tk.Label(frm_create, text='Yard size, square footage')
ent_size = tk.Entry(frm_create, width=15)
lbl_maxPlants = tk.Label(frm_create, text='Use maximum # of plants')
btn_True = tk.Radiobutton(frm_create, text='True',
                                            var=maxPlants,
                                            value="True")
btn_False = tk.Radiobutton(frm_create, text='False',
                                        var=maxPlants,
                                        value="False")
lbl_feature = tk.Label(frm_create, text='Organize plants by:')
feat = tk.StringVar(frm_create)
feat.set(plant_features[0])
dropDown = tk.OptionMenu(frm_create, feat, *plant_features)
btn_create = tk.Button(frm_create,
                       text='Create garden',
                       command= lambda: newGarden(int(ent_count.get()),
                                                  int(ent_size.get()),
                                                  maxPlants.get(),
                                                  feat.get()))
lbl_count.pack()
ent_count.pack()
lbl_size.pack()
ent_size.pack()
lbl_maxPlants.pack()
btn_True.pack()
btn_False.pack()
lbl_feature.pack()
dropDown.pack()
btn_create.pack()

frm_plants = tk.Frame(window)
lst_plants = tk.Listbox(frm_plants, height=20)
for key, value in start_garden.plants.items():
    lst_plants.insert(tk.END, key)
lst_plants.bind('<<ListboxSelect>>', show_data)
btn_remove = tk.Button(frm_plants,
                       text="Remove",
                       command= lambda: lst_plants.delete(lst_plants.curselection()))

frm_info = tk.Frame(window)

# gridding----------------------------------------------------------------------

n.grid(row=0, column=0, sticky='nsew')
n.add(frm_create, text='Create')
n.add(frm_add, text='Add')
frm_info.grid(row=1, column=1)
frm_plants.grid(row=1, column=0)

lbl_add.pack()
# lbl_plant.pack()
# lbl_pattern.pack(fill=tk.X)
lst_plants.pack()
btn_remove.pack()

window.mainloop()
