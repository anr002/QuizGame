import requests
from bs4 import BeautifulSoup

url = "https://smite.fandom.com/wiki/Smite_Wiki"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img', {'class': 'lazyload'})

image_urls = [img['data-src'] for img in images if 'data-src' in img.attrs and 'T_' in img['data-src']]

gods = {url.split('T_')[1].split('_')[0]: url for url in image_urls if 'T_' in url}


gods_list = [{"name": god, "icon": url} for god, url in gods.items()]

# 
#for god, url in gods.items():
#   print(f"God: {god}, URL: {url}")




with open('index2.html', 'w') as f:
    f.write('<html>\n<body>\n')
    for god in gods_list:
        f.write(f"<p>God: {god['name']}, Icon: <img src='{god['icon']}'/></p>\n")
    f.write('</body>\n</html>')

import json

gods_json = json.dumps(gods_list)

with open('gods.json', 'w') as f:
    f.write(gods_json)