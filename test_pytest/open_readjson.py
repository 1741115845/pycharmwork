import json


def read_json():
    return json.load(open('login.json','r',encoding='utf-8'))
