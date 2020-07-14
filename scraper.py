from bs4 import BeautifulSoup
import requests
from gardens import *
import urllib.request
from PIL import ImageTk, Image
import csv
import re
import os, ssl

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
              'Hardiness Rating:',
              'Height:',
              'Spread:',
              'Colour in Summer:',
              'Colour in Fall:',
              'Colour (petals):',
              'Slide Show:']


with open('plantList.csv', mode='w') as csv_file:
    fields = ['name', 'growth_rate', 'exposure', 'soil', 'hardiness', 'water',
                                                         'height',
                                                         'spread',
                                                         'colourInSummer',
                                                         'colourInFall',
                                                         'colourPetals',
                                                         'slideShow']
    writer = csv.DictWriter(csv_file, fieldnames= fields)
    writer.writeheader()

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
        water = ""
        hardiness = ""
        height = ""
        spread = ""
        colourInSummer = ""
        colourInFall = ""
        colourPetals = ""
        slideShow = ""
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
                elif i.text == 'Height:':
                    height = i.find_next('td').text
                elif i.text == 'Spread:':
                    spread = i.find_next('td').text
                elif i.text == 'Colour in Summer:':
                    colourInSummer = i.find_next('td').text
                elif i.text == 'Colour in Fall:':
                    colourInFall = i.find_next('td').text
                elif i.text == 'Colour (petals):':
                    colourPetals = i.find_next('td').text
        imageLink = info.find("div", class_= "slideshow")
        if imageLink == None:
            continue
        imageLink = imageLink.a['href']
        imagePage = requests.get(BASE_URL+imageLink)
        imagePageInfo = BeautifulSoup(imagePage.content, 'html.parser')
        images = imagePageInfo.find_all('img', {'src':re.compile('.jpg')})
        urlImage = BASE_URL+images[0]['src']
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context
        pic = urllib.request.urlretrieve(urlImage,
                                        f'plantImages/{name.replace(" ","")}.jpg')
        photo = Image.open(pic[0])
        slideShow = photo

        writer.writerow({'name'          : ' '.join(name.split()),
                        'growth_rate'    : ' '.join(growth_rate.split()),
                        'exposure'       : ' '.join(exposure.split()),
                        'soil'           : ' '.join(soil.split()),
                        'hardiness'      : ' '.join(hardiness.split()),
                        'water'          : ' '.join(water.split()),
                        'height'         : height.split(' ')[-1][:-1],
                        'spread'         : spread.split(' ')[-1][:-1],
                        'colourInSummer' : ' '.join(colourInSummer.split()),
                        'colourInFall'   : ' '.join(colourInFall.split()),
                        'colourPetals'   : ' '.join(colourPetals.split()),
                        'slideShow'      : slideShow})
