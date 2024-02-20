from bs4 import BeautifulSoup
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Safari()
browser.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

scraped_data = []

def scrape():
    for i in range(1,2):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star_table = soup.find_all("table", attrs={"class", "wikitable"})[2]

        table_body = bright_star_table.find("tbody")

        table_rows = table_body.find_all("tr")

        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            scraped_data.append(row)

scrape()

stars_data = []

for i in range(0, len(scraped_data)):
    star_dict = {
        "brown dwarf": scraped_data[i][0],
        "constellation": scraped_data[i][1],
        "right ascension": scraped_data[i][2],
        "declination": scraped_data[i][3],
        "app. mag.": scraped_data[i][4],
        "distance": scraped_data[i][5],
        "spectral type": scraped_data[i][6],
        "mass": scraped_data[i][7],
        "radius": scraped_data[i][8],
        "discovery year": scraped_data[i][9],
    }
    stars_data.append(star_dict)

headers = ["brown dwarf", "constellation", "right ascension","declination", "app. mag.", "distance", "spectral type", "mass", "radius", "discovery year"]
df = pd.DataFrame(stars_data, columns=headers)
df.to_csv("brown dwarfs.csv",index=True, index_label="id")


browser.quit()

