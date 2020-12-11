import requests
from pprint import pprint
with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()


def get_photos(id, version):
    url = 'https://api.vk.com/method/'
    token_id = token
    user_id = id
    photo_url = url + 'photos.get'
    photo_params = {
        'v': version,
        'access_token': token_id,
        'owner_id': user_id,
        'album_id': 'profile',
        'extended': 1,
        'count': 5,
        'photo_sizes': 1
    }
    res = requests.get(photo_url, params=photo_params)
    return res.json()

photos = get_photos(40242864, '5.126')
name = []
url = []
for item in photos['response']['items']:
    name.append(item['likes']['count'])
    url.append(item['sizes'][9]['url'])

ph = dict(zip(name, url))
# print(*ph.values())
with open('tokenya.txt', 'r') as file_object:
    tokenya = file_object.read().strip()

HEADERS = {'Authorization': tokenya}
for like, photo in ph.items():
    resp = requests.get(
        'https://cloud-api.yandex.net/v1/disk/resources/upload',
        params={'url': photo, 'path': '/diploma/'+str(like)+'.jpg'},
        headers=HEADERS
    )
    resp.raise_for_status()
    d = resp.json()
    href = d['href']
    resp2 = requests.put(href)
    resp2.raise_for_status()
