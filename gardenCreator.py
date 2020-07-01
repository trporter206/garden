import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from gardens import *
import csv
import random

def createGardenHelper(count, size, max, feature, val):
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
            if row[val_index] == val:
                newGarden.add_plant(row[0])
                if len(newGarden.plants) == count:
                    return newGarden

            line +=1
    return newGarden
