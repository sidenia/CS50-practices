# https://itunes.apple.com/search?entity=song&limit=1&term=weezer  this limit will bring just 1 song of the band weezer

import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

band = sys.argv[1] 
response = requests.get(f'https://itunes.apple.com/search?entity=song&limit=50&term={band}')
data = response.json()

for result in data['results']:
  print(result['trackName'])