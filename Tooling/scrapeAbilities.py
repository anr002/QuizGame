import os
import requests
from bs4 import BeautifulSoup
import json
import re

base_url = "https://smite.fandom.com"

with open('gods.json', 'r') as f:
    gods_list = json.load(f)

ability_names = ["passive"] + [f"ability_{i}" for i in range(1, 13)]

for god in gods_list:
    god_name = god['name']
    if god_name == "Chang E":
        god_name = "Chang'e"
    god_url = base_url + "/wiki/" + god_name.replace(" ", "_").replace("'", "%27")
    response = requests.get(god_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img', {'src': re.compile(r'Icons_.*\.png')})

    os.makedirs(os.path.join("God Abilities", god['name']), exist_ok=True)

    for i, img in enumerate(img_tags):
        if i >= len(ability_names):
            break
        icon_url = img['src']
        icon_response = requests.get(icon_url)
        with open(os.path.join("God Abilities", god['name'], f"{ability_names[i]}.png"), 'wb') as f:
            f.write(icon_response.content)