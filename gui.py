import tkinter as tk
from gardens import *
from main import *

num_plants = 15

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
    lbl_plant["text"] = searchPlant(lst_plants.get(index))

def newGarden(*args):
    newGarden = create_random_garden(num_plants)
    lst_plants.delete(0,tk.END)
    for key, value in newGarden.plants.items():
        lst_plants.insert(tk.END, key)

# window and widgets------------------------------------------------------------

window = tk.Tk()
window.title("Gardener")
window.rowconfigure([0,1], minsize=200, weight=1)
window.columnconfigure([0,1], minsize=200, weight=1)

btn_createGarden = tk.Button(window, text='New Garden', command=newGarden)

lst_plants = tk.Listbox(window, height=10)
# for key, value in garden.plants.items():
#     lst_plants.insert(tk.END, key)
lst_plants.bind('<<ListboxSelect>>', show_data)

lbl_plant = tk.Label(window, text='Plant info')

# gridding----------------------------------------------------------------------

# lst_frame.grid(row=0, column=0, sticky='nsew')
btn_createGarden.grid(row=0, column=0)
lst_plants.grid(row=1, column=0)
lbl_plant.grid(row=0, column=1, sticky='nsew')

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
