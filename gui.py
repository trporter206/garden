import tkinter as tk
import csv
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
from PIL import ImageTk, Image
from gardens import *
from gardenCreator import *

garden = Garden()

borderEffects = {
    "flat"   : tk.FLAT,
    "sunken" : tk.SUNKEN,
    "raised" : tk.RAISED,
    "groove" : tk.GROOVE,
    "ridge"  : tk.RIDGE,
}

displayed_features = [
    'growth_rate',
    'exposure',
    'soil',
    'hardiness',
    'water',
    'height',
    'spread',
    'colourInSummer',
    'colourInFall',
    'colourPetals',
]

choosable_features = [
    'growth_rate',
    'exposure',
    'soil',
    'hardiness',
    'water',
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
        label = tk.Label(frm_info, text=str(displayed_features[i])+': '+str(val))
        label.pack()

def show_data(*args):
    index = lst_plants.curselection()
    plant_data = Garden.searchPlant(lst_plants.get(index[0]).strip())
    plantTextFormat(plant_data)

def newGarden(size, max, feature, val):
    newGarden = Garden()
    newGarden = createGardenHelper(newGarden, size, max, feature, val)
    garden = newGarden
    del newGarden
    lst_plants.delete(0,tk.END)
    for key, value in garden.plants.items():
        lst_plants.insert(tk.END, key)

# def addPlant_helper(plant):
#     newPlant = searchPlant(plant)
#     if newPlant == None:
#         return None
#     else:
#         lst_plants.insert(tk.END, newPlant[0])
#         return True

def addPlant(plant, garden, *args):
    garden.add_plant(plant, garden)
    if length1 < length2:
        lbl_add['text'] = f'{plant} not in database'
    else:
        for key, value in garden.plants.items():
            lst_plants.insert(tk.END, key)
        lbl_add['text'] = f'{plant} added to garden'

def removePlant(plant, garden, *args):
    garden.remove_plant(plant)

def updateOptions(*args):
    feature = Garden.plant_values[feat.get()]
    feat_option.set(feature[0])
    menu = dropDown2['menu']
    menu.delete(0, 'end')

    for val in feature:
        menu.add_command(label=val, command=lambda option=val: feat_option.set(option))

def openFile():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    lst_plants.delete(0, tk.END)
    with open(filepath, "r") as input_file:
        next(input_file)
        row = 0
        for line in input_file:
            lst_plants.insert(row, line)
            row+=1

def saveFile():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "a") as output_file:
        for plant in lst_plants.get(0, tk.END):
            output_file.write("\n")
            output_file.write(plant)

# widgets/frames----------------------------------------------------------------

n = Notebook(window)

frm_add = tk.Frame(n)
lbl_plantName = tk.Label(frm_add, text='Enter plant name: ')
ent_plant = tk.Entry(frm_add, width=30)
btn_addPlant = tk.Button(frm_add,
                         text='Add plant',
                         command= lambda: addPlant(ent_plant.get(), garden))
lbl_add = tk.Label(frm_add)
lbl_plantName.pack()
ent_plant.pack()
btn_addPlant.pack()
lbl_add.pack()

frm_create = tk.Frame(n)
maxPlants = tk.StringVar(frm_create)
maxPlants.set("False")
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
feat_option = tk.StringVar(frm_create)
feat.trace('w', updateOptions)
dropDown1 = tk.OptionMenu(frm_create, feat, *choosable_features)
dropDown2 = tk.OptionMenu(frm_create, feat_option, '')
feat.set(choosable_features[0])

btn_create = tk.Button(frm_create,
                       text='Create garden',
                       command= lambda: newGarden(int(ent_size.get()),
                                                  maxPlants.get(),
                                                  feat.get(),
                                                  feat_option.get()))
lbl_size.pack()
ent_size.pack()
lbl_maxPlants.pack()
btn_True.pack()
btn_False.pack()
lbl_feature.pack()
dropDown1.pack()
dropDown2.pack()
btn_create.pack()

frm_plants = tk.Frame(window)
lst_plants = tk.Listbox(frm_plants, height=20)
for key, value in garden.plants.items():
    lst_plants.insert(tk.END, key)
lst_plants.bind('<<ListboxSelect>>', show_data)
btn_remove = tk.Button(frm_plants,
                       text="Remove",
                       command= lambda: lst_plants.delete(lst_plants.curselection()))
btn_open = tk.Button(frm_plants, text="Open", command=openFile)
btn_save = tk.Button(frm_plants, text="Save As", command=saveFile)
lbl_add.pack()
lst_plants.pack()
btn_remove.pack()
btn_open.pack()
btn_save.pack()

frm_info = tk.Frame(window)

# gridding----------------------------------------------------------------------

n.grid(row=0, column=0, sticky='nsew')
n.add(frm_create, text='Create')
n.add(frm_add, text='Add')
frm_info.grid(row=1, column=1)
frm_plants.grid(row=1, column=0)

window.mainloop()
