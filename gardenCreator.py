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
        line = 0
        firstline = True
        val_index = ''
        for row in csv_reader:
            if firstline:
                firstline = False
                val_index = row.index(feature)
                continue
            # where the action starts
            if row[val_index] == val:
                print(row)
                if (newGarden.size+float(row[7])) < size:
                    newGarden.add_plant(row[0])
                else:
                    return newGarden

            line +=1
    return newGarden
