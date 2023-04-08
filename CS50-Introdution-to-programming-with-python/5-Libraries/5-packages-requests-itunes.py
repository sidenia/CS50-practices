# https://itunes.apple.com/search?entity=song&limit=1&term=weezer  this limit will bring just 1 song of the band weezer

import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

band = sys.argv[1] 
response = requests.get(f'https://itunes.apple.com/search?entity=song&limit=1&term={band}')
# print(response.json())
prettyPrinting = json.dumps(response.json(), indent=2)
print(prettyPrinting)