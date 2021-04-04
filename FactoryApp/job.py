from bs4 import BeautifulSoup
from adapter import RedisAdapter

import requests
import json

service_url = "143.198.77.145:8000/item"

def get_entry(url):
    print("Work started")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }
    session_resp = requests.Session()
    response_from_root_page = session_resp.get(url, headers=headers)
    if response_from_root_page is None:
        response_from_root_page = session_resp.get(url, headers=headers, cookies=response_from_root_page.cookies)

    soup = BeautifulSoup(response_from_root_page.text, 'lxml-xml')
    ads_data_string = soup.find('div', {'class': 'js-initial'}).get('data-state')
    ads_data_string = ads_data_string.replace('&quot', '"').replace(";","").replace(r"\\", "")

    

    ads_data_dict = json.loads(ads_data_string)
    for ad in ads_data_dict.get('catalog').get('items'):
        if ad['type'] == 'item':
            # Проверка на совпадение в базе
            ad_id = ad.get('id')
            if not RedisAdapter.database_match_check(ad_id):
                new_ad = {
                    "id": ad_id,
                    "title": ad.get('title'),
                    "date": ad.get('iva').get('DateInfoStep')[0].get('payload').get('absolute'),
                    "url_path": 'https://www.avito.ru' + ad.get('urlPath')
                }
                RedisAdapter.create(new_ad)
                print("Result: new ad")
                post_result = requests.post(service_url, data={
                    "id": ad_id,
                    "name": ad.get("title"),
                    "url": 'https://www.avito.ru' + ad.get('urlPath'),
                    "body": ad.get('iva').get('DateInfoStep')[0].get('payload').get('absolute'),
                })

                return RedisAdapter.get(ad_id)
            else:
                print("Result: Existeed")
                return 'exists'
        break