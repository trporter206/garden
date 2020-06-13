import tkinter as tk
from tkinter import messagebox
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

# methods-----------------------------------------------------------------------

def show_data(*args):
    index = lst_plants.curselection()
    lbl_plant["text"] = searchPlant(lst_plants.get(index[0]))
    pattern = ImageTk.PhotoImage(file="plant patterns/"+lst_plants.get(index)+".jpg")
    lbl_pattern['image'] = pattern
    lbl_pattern.image = pattern

def newGarden(count):
    newGarden = create_random_garden(count)
    lst_plants.delete(0,tk.END)
    for key, value in newGarden.plants.items():
        lst_plants.insert(tk.END, key)

def addPlant_helper(plant):
    print(plant)
    newPlant = searchPlant(plant)
    if newPlant == None:
        return None
    lst_plants.insert(tk.END, newPlant.name)


def addPlant(*args):
    entry = tk.Entry(frm_info, width=30)
    search = tk.Button(frm_info, text='Add')
    search.bind("<Button-1>", addPlant_helper(entry.get()))
    entry.pack()
    search.pack()
    print(entry.get())
    if addPlant_helper(entry.get()) == None:
        tk.messagebox.showerror('No Plant', "Plant not in database")

def add_tool():
    pass

def current_tool(*args):
    frm_info = tk.Frame(window)
    frm_info.grid(row=0, column=1, sticky='nsew')
    if tool.get() == 'create':
        lbl_count = tk.Label(frm_info, text='How many plants?')
        ent_count = tk.Entry(frm_info, width=30)
        ent_numPlants = tk.Button(frm_info, text='Create garden',
                                            command= lambda: newGarden(int(ent_count.get())))
        lbl_count.pack()
        ent_count.pack()
        ent_numPlants.pack()
    elif tool.get() == 'add':
        add_tool()





# window and widgets------------------------------------------------------------

window = tk.Tk()
window.title("Gardener")
window.rowconfigure([0,1,2], minsize=200, weight=1)
window.columnconfigure([0,1], minsize=200, weight=1)

tool = tk.StringVar(window)

frm_btns = tk.Frame(window)
frm_info = tk.Frame(window)

btn_createGarden = tk.Radiobutton(frm_btns, text='New Garden',
                                            var=tool,
                                            value="create",
                                            command=current_tool)
btn_addPlant = tk.Radiobutton(frm_btns, text='Add Plant',
                                        var=tool,
                                        value="add",
                                        command=current_tool)

lst_plants = tk.Listbox(window, height=10)
for key, value in start_garden.plants.items():
    lst_plants.insert(tk.END, key)
lst_plants.bind('<<ListboxSelect>>', show_data)

lbl_plant = tk.Label(frm_info)
lbl_pattern = tk.Label(frm_info)

# gridding----------------------------------------------------------------------

frm_btns.grid(row=0, column=0, sticky='nsew')
frm_info.grid(row=1, column=1, sticky='nsew')
lst_plants.grid(row=1, column=0)

btn_createGarden.pack(pady=10)
btn_addPlant.pack(pady=5)
lbl_plant.pack()
lbl_pattern.pack()

window.mainloop()














# example form GUI--------------------------------------------------------------

# labels = [
#     'First name: ',
#     'Last name: ',
#     'Address 1: ',
#     'Address 2: ',
#     'City: ',
#     'Province: ',
#     'Postal Code: ',
#     'Country: '
# ]
#
# window = tk.Tk()
# window.title('Entry Form')
#
# entries = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
# entries.pack()
#
# for i in range(len(labels)):
#     label = tk.Label(master=entries, text=labels[i])
#     entry = tk.Entry(master=entries, width=30)
#     label.grid(row=i, column=0, sticky='w')
#     entry.grid(row=i, column=1)
#
# buttons = tk.Frame()
# buttons.pack(fill=tk.X, ipadx=5, ipady= 5)
#
# clearButton = tk.Button(master= buttons, text='Clear')
# clearButton.bind("<Button-1>", handle_click)
# clearButton.pack(side= tk.RIGHT, ipadx=10)
#
# submitButton = tk.Button(master= buttons, text='clear')
# submitButton.pack(side= tk.RIGHT, ipadx=10)
#
# window.mainloop()

# example simple counter-------------------------------------------------------

# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
# window = tk.Tk()
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#
# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")
#
# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")
#
# window.mainloop()

# example dice roller-----------------------------------------------------------

# def roll():
#     lbl_roll["text"] = f"{random.randint(1,6)}"
#
# window = tk.Tk()
# window.rowconfigure([0,1], minsize=50, weight=1)
# window.columnconfigure(0, minsize=50, weight=1)
#
# btn_roll = tk.Button(master=window, text="Roll", command=roll, relief= tk.RAISED)
# btn_roll.grid(row=0, column=0, sticky="nsew")
#
# lbl_roll = tk.Label(master=window, text="0")
# lbl_roll.grid(row=1, column=0)
#
# window.mainloop()

# example temperature converter-------------------------------------------------

# def convert():
#     fahrenheit = ent_temp.get()
#     celsius = (5/9) * (float(fahrenheit) - 32)
#     lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
#
# window = tk.Tk()
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0,1,2], minsize=50, weight=1)
#
# ent_temp = tk.Entry(master=window, width=5)
# lbl_temp = tk.Label(master=window, text='F')
# ent_temp.grid(row=0, column=0)
# lbl_temp.grid(row=0, column=0, sticky='e')
#
# btn_convert = tk.Button(master=window, text="Convert", command=convert)
# btn_convert.grid(row=0, column=1, sticky='nsew')
#
# lbl_result = tk.Label(master=window)
# lbl_result.grid(row=0, column=2)
#
# window.mainloop()

# example text editor-----------------------------------------------------------
# from tkinter.filedialog import askopenfilename, asksaveasfilename
#
# def open_file():
#     filepath = askopenfilename(
#         filetypes = [("Text Files", "*.txt"), ("All Files, *.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete("1.0", tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")
#
# def save_file():
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")
#
# window = tk.Tk()
# window.title('Text Editor')
#
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
#
# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text='Save as...', command=save_file)
#
# btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky='ew', padx=5)
# fr_buttons.grid(row=0, column=0, sticky='ns')
# txt_edit.grid(row=0, column=1, sticky='nsew')
#
# window.mainloop()
