from bs4 import BeautifulSoup
import requests

URL = "https://plantdatabase.kpu.ca/plant/siteIndex"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
