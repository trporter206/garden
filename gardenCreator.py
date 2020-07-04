import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from gardens import *
import csv
import random

def createGardenHelper(size, max, feature, val):
    newGarden = Garden("New Garden")
    if feature == '':
        return newGarden
    newGarden.maximumSize = size
    with open('plantList.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        firstline = True
        val_index = ''
        possible_plants = []
        for row in csv_reader:
            if firstline:
                firstline = False
                val_index = row.index(feature)
                continue
            if row[7] == '':
                spread = 0
            else:
                spread = float(row[7])
            if row[val_index] == val:
                if (newGarden.size+spread) < size:
                    newGarden.add_plant(row[0])
                else:
                    return newGarden
            
    return newGarden
