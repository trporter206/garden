import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from gardens import *
import csv
import random

def createGardenHelper(count, size, max, feature):
    print(count, size, max, feature)
    newGarden = Garden("New Garden")
    newGarden.maximumSize = size
    with open('plantList.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line = 0
        firstline = True
        for row in csv_reader:
            if firstline:
                firstline = False
                continue
            nums = random.sample(range(60), count)
            if line in nums:
                newGarden.add_plant(row[0])
                if len(newGarden.plants) == count:
                    return newGarden

            line +=1
    return newGarden
