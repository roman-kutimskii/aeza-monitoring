import pprint
import json

import requests
from bs4 import BeautifulSoup

from config import URL


def parse_data() -> bool:
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find('script', id='__NEXT_DATA__', type='application/json')

    if script_tag is not None:
        script_content = script_tag.string

        try:
            data = json.loads(script_content)
            locations = data.get('props').get('pageProps').get('locations')
            return next((location for location in locations if location.get('id') == 23), None).get('hasProducts')
        except json.JSONDecodeError:
            print('Ошибка при декодировании JSON.')
            return False
    else:
        print('Тег <script> с id=\'__NEXT_DATA__\' не найден.')
        return False
