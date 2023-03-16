import os

import requests


def internal_call_get(to_service_id, uri, param_map, headers):
    from_service_id = os.getenv('SERVICE_ID')
    host = 'http://%s-%s.dycloud.service%s' % (from_service_id, to_service_id, uri)
    try:
        response = requests.get(host, params=param_map, headers=headers)
        res = response.text
        print(res)
        response.close()
        return res
    except:
        print('http get failed')
        return 'http get failed'


def internal_call_post(to_service_id, uri, body, headers):
    from_service_id = os.getenv('SERVICE_ID')
    host = 'http://%s-%s.dycloud.service%s' % (from_service_id, to_service_id, uri)
    try:
        response = requests.post(host, json=body, headers=headers)
        res = response.text
        print(res)
        response.close()
        return res
    except :
        print('http post failed')
        return 'http post failed'
