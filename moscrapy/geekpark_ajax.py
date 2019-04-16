from urllib.parse import urlencode
import requests

def get_page(offset):
    params = {
        'page': '10',
    }

    url = 'https://mainssl.geekpark.net/api/v2?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
    except requests.ConnectionError:
        print('ERROR')

