import configparser
config = configparser.ConfigParser()
config.read('Config.ini')

host = config['DataBase']['host']
db_port = config['DataBase']['port']
user = config['DataBase']['user']
us_password = config['DataBase']['us_password']
db_name = config['DataBase']['db_name']
flagCreateDataBase = config.getboolean('DataBase', 'flag_database')
flagCreateTable = config.getboolean('DataBase', 'flag_table')