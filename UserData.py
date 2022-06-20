import configparser
import json

config = configparser.ConfigParser()
config.read('Config.ini')

phone = config['User']['phone']
password = config['User']['Password'].encode('utf-8')
address_producer = config['User']['address']
domen = 'auth/login'
region = json.loads(config['User']['region'])