from pprint import pprint

import requests

HEADERS = {'Authorization': 'OAuth '}

resp = requests.get(
    'https://cloud-api.yandex.net/v1/disk/resources/upload',
    params={'path': 'VL_Kursach.docx', 'overwrite': 'true'},
    headers=HEADERS
)

resp.raise_for_status()
d = resp.json()

href = d['href']

with open('VL_Kursach.docx', 'rb') as f:
    resp2 = requests.put(href, files={'file': f})

resp2.raise_for_status()
pr
ggff