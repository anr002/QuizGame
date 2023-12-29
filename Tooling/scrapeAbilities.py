import os
import requests
from bs4 import BeautifulSoup
import json
import re

base_url = "https://smite.fandom.com"

with open('gods.json', 'r') as f:
    gods_list = json.load(f)

ability_names = ["passive", "ability_1", "ability_2", "ability_3", "ability_4", "ability_5", "ability_6", "ability_7", "ability_8", "ability_9", "ability_10"]

for god in gods_list:
    god_url = base_url + "/wiki/" + god['name'].replace(" ", "_")
    response = requests.get(god_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img', {'src': re.compile(r'Icons_.*\.png')})

    os.makedirs(god['name'], exist_ok=True)

    for i, img in enumerate(img_tags):
        icon_url = img['src']

        icon_response = requests.get(icon_url)
        with open(os.path.join(god['name'], f"{ability_names[i]}.png"), 'wb') as f:
            f.write(icon_response.content)