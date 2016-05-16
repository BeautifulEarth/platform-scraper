__author__ = 'chrisshroba'

import requests
import requests.auth
from pprint import pprint
from operator import itemgetter

# access_token = '22273448-4jhfwz9B-WWoUjqhHzl-Ybqv_kE'


client_auth = requests.auth.HTTPBasicAuth('nOGP17UUkwG-2g', 'AX0E8vS4g7CCYNfR_7DpfLiv6A8')
post_data = {"grant_type": "password", "username": "picturescraper", "password": "8u\*}f(wtbh8gp&"}
headers = {"User-Agent": "Scraperoony/0.1 by picturescraper"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
access_token = response.json().get('access_token')
print(access_token)

class Post(object):
    def __init__(self):
        pass

def foo():

    headers = {"Authorization": "bearer {}".format(access_token), "User-Agent": "Scraperoony/0.1 by picturescraper"}
    response = requests.get("https://oauth.reddit.com/r/earthporn", headers=headers)
    data = response.json()

    d = data['data']['children']

    d = list(map(itemgetter('data'), d))

    d.sort(key=itemgetter('ups'))

    for i in d:
        fields = [
            'name',
            'author',
            'ups',
            'url'
        ]
        print('\n\n=================')
        for field in i.keys():
            print('{}:\t{}'.format(field, i[field]))
            pass

foo()