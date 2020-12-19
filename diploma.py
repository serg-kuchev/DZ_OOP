import requests
import time
from tqdm import tqdm
import json


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

idvk = int(input('Введите id пользователя: '))
tokenya = str(input('Введите токен вашего Яндекс.Диска: '))

loop = tqdm(total=1, position=0, leave=False)
loop_1 = tqdm(total=5, position=0, leave=False)

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()

photos = get_photos(idvk, '5.126')
name = []
url = []
data = []
for item in photos['response']['items']:
    loop.set_description('Загружаю URL фотографий...'.format(item))
    name.append(item['likes']['count'])
    b = len(item['sizes'])
    url.append(item['sizes'][b-1]['url'])
    d = {
        'file_name': str(item['likes']['count']) + '.jpg',
        'size': str(item['sizes'][b-1]['type'])
    }
    data.append(d)
    time.sleep(2)
    loop.update(1)
with open('photos_info.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

ph = dict(zip(name, url))

HEADERS = {'Authorization': 'OAuth'+' '+str(tokenya)}
resp1 = requests.put(
    'https://cloud-api.yandex.net/v1/disk/resources',
    params={'path': 'diploma'},
    headers=HEADERS
)
resp1.raise_for_status()


for like, photo in ph.items():
    loop_1.set_description('Загружаю фотографии на Яндекс.Диск...'.format(like))
    resp = requests.post(
        'https://cloud-api.yandex.net/v1/disk/resources/upload',
        params={'url': photo, 'path': '/diploma/'+str(like)+'.jpg', 'disable_redirects': 'false'},
        headers=HEADERS
    )
    resp.raise_for_status()

    loop_1.update(1)
