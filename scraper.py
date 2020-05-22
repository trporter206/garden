from bs4 import BeautifulSoup
import requests
from gardens import *
import csv

URL = "https://plantdatabase.kpu.ca/plant/siteIndex"
BASE_URL = "https://plantdatabase.kpu.ca"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

common_names = soup.find_all('span', class_="common_name")
plant_links = soup.find_all('a', class_="preview")

plant_keys = ['Growth Rate:',
              'Exposure:',
              'Soil/ Growing Medium:',
              'Water Use:',
              'Hardiness Rating:']

plant_list = {}

for plant in plant_links:
    name = plant.find_next('td').text
    print(name)
    link = str(plant['href'])
    plant_page = requests.get(BASE_URL+link)
    info = BeautifulSoup(plant_page.content, 'html.parser')
    page_info = info.find_all('td')
    growth_rate = ""
    exposure = ""
    soil = ""
    hardiness = ""
    water = ""
    for i in page_info:
        if i.text in plant_keys:
            if i.text == 'Growth Rate:':
                growth_rate = i.find_next('td').text
            elif i.text == 'Exposure:':
                exposure = i.find_next('td').text
            elif i.text == 'Soil/ Growing Medium:':
                soil = i.find_next('td').text
            elif i.text == 'Hardiness Rating:':
                hardiness = i.find_next('td').text
            elif i.text == 'Water Use:':
                water = i.find_next('td').text
        if water == "":
            water = "NA"

    p = Plant(name, growth_rate, hardiness, exposure, soil, water)
    plant_list[p.name] = {
        'Growth Rate': ' '.join(growth_rate.split()),
        'Exposure'   : ' '.join(exposure.split()),
        'Soil'       : ' '.join(soil.split()),
        'Hardiness'  : ' '.join(hardiness.split()),
        'Water'      : ' '.join(water.split())
    }

with open('plants.csv', mode='w') as csv_file:
    fields = ['name', 'growth_rate', 'exposure', 'soil', 'hardiness', 'water']
    writer = csv.DictWriter(csv_file, fieldnames= fields)
    writer.writeheader()
    for key, value in plant_list.items():
       writer.writerow({'name'       : key,
                        'growth_rate': value['Growth Rate'],
                        'exposure'   : value['Exposure'],
                        'soil'       : value['Soil'],
                        'hardiness'  : value['Hardiness'],
                        'water'      : value['Water']})
