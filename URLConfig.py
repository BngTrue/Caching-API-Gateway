import requests
import base64
import json
import datetime
from collections import OrderedDict
from UserData import password, domen, address_producer, phone, region

def getDictData():
    response = requests.get(address_producer + domen, headers=myTok)
    temp = json.loads(response.text)
    return temp

def getDictSortData():
    response = requests.get(address_producer + domen, headers=myTok, params={'regionIds': region})
    temp = json.loads(response.text)
    return temp

def createCitiesData():
    CitiesData = []
    for val in getDictData():
        CitiesData.append((val['created'], val['updated'], val['id'], val['name'], val['regionId']))
    return CitiesData

def createCategoriesData():
    CategoriesData = []
    for val in getDictData():
        CategoriesData.append((val['created'], val['updated'], val['id'], val['name']))
    return CategoriesData

def createRegionsData():
    RegionsData = []
    for val in getDictData():
        RegionsData.append((val['created'], val['updated'], val['id'], val['name']))
    return RegionsData

def createShopsData():
    ShopsData = []
    content = getDictData()['content']
    for val in content:
        ShopsData.append((val['created'], val['updated'], val['id'], val['brandId'], val['cityId'], (val['closeDate']),
                         val['location'], val['phone'], val['regionId'], json.dumps(val['workHours']), val['coordinates']['longitude'], val['coordinates']['latitude']))
    return ShopsData

def createBrandsData():
    BrandsData = []
    content = getDictData()['content']
    for val in content:
        d = val['logoImages']
    print(d)
    #jsd = json.dumps(d)
    #print(jsd)
    for val in content:
        BrandsData.append((val['created'], val['updated'], val['id'], val['name'], val['shortDescription'], val['description'],
                           val['description_html'], json.dumps(val['logoImages']), json.dumps(val['photo']), val['portalLink'], val['website']))
    return BrandsData

def createPromoActionsData():
    PromoActionsData = []
    content = getDictSortData()['content']
    for val in content:
        PromoActionsData.append((val['created'], val['updated'], val['specialConditionsType'], val['id'], val['bonusType'],
                                 val['brandId'], val['cashbackAmount'], json.dumps(val['categoryIds']), val['conditions'], val['conditions_html'],
                                 val['endedAt'], val['mechanicsDescription'], val['mechanicsDescription_html'], val['name'], val['percent'],
                                 json.dumps(val['photoSets']), val['portalLink'], json.dumps(val['regionIds']), val['rules_html'], json.dumps(val['shopsIds']),
                                 json.dumps(val['cardProgramCodes']), val['startedAt']))
    return PromoActionsData

password = base64.b64encode(password)
password = str(password.decode('utf-8'))

data = {'phone': phone, 'password': password}

response = requests.post(address_producer+domen, json=data)

token = json.loads(response.text)

access = token['accessToken']

myTok = {'Authorization': f'Bearer {access}'}

domen = 'cities'
CitiesData = createCitiesData()

domen = 'categories'
CategoriesData = createCategoriesData()

domen = 'regions'
RegionsData = createRegionsData()

domen = 'shops'
ShopsData = createShopsData()

domen = 'brands'
BrandsData = createBrandsData()

domen = 'promo-actions'
PromoActionsData = createPromoActionsData()
