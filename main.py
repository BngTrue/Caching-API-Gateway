import json
import pymysql
from DBParam import host, user, us_password, db_name, db_port, flagCreateTable, flagCreateDataBase
from URLConfig import CitiesData, RegionsData, CategoriesData, ShopsData, PromoActionsData, BrandsData
import configparser

def configParser(file, section, operand, value):
    config = configparser.ConfigParser()
    config.read(file)
    config[section][operand] = value
    with open(file, 'w') as configfile:
        config.write(configfile)


def Connect(db_name):
    return pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=us_password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

try:
    connection = Connect(db_name)
    print('success')
    try:
        # cursor = connection.cursor()
        with connection.cursor() as cursor:
            if(flagCreateDataBase):
                create_table_query = "CREATE DATABASE TEST_DATABASE;"
                cursor.execute(create_table_query)
                configParser('Config.ini', 'DataBase', 'db_name', 'test_database')
                configParser('Config.ini', 'DataBase', 'flag_database', 'false')
                connection.commit()
                print('DataBase created!')
            if(flagCreateTable):
                connection = Connect('test_database')
                cursor = connection.cursor()

                create_table_query = "CREATE TABLE Brands (created TEXT, updated TEXT, id TEXT, name TEXT," \
                                     " shortDescription TEXT, description TEXT, description_html TEXT," \
                                     " logoImages JSON, photo JSON, portalLink TEXT, website TEXT);"
                cursor.execute(create_table_query)
                # created and updated to date-time
                # brands completed

                create_table_query = "CREATE TABLE Categories (created TEXT, updated TEXT, id INT, name TEXT);"
                cursor.execute(create_table_query)
                # created and updated to date-time
                #Categories completed

                create_table_query = "CREATE TABLE Cities (created TEXT, updated TEXT, id INT, name TEXT, regionId INT);"
                cursor.execute(create_table_query)
                # created and updated to date-time
                #cities completed

                create_table_query = "CREATE TABLE PromoActions (created TEXT, updated VARCHAR(30), " \
                                     "specialConditionsType ENUM('better-with-premium', 'only-for-premium'), id TEXT, bonusType ENUM('cashback', 'promocode', 'raffle_p', 'point', 'reversal')," \
                                     "brandId TEXT, cashbackAmount TEXT, categoryIds JSON, conditions TEXT, conditions_html TEXT, endedAt DATE," \
                                     " mechanicsDescription	TEXT, mechanicsDescription_html TEXT, name TEXT, percent FLOAT, photoSets JSON, portalLink TEXT," \
                                     " regionIds JSON, rules_html TEXT, shopsIds JSON, cardProgramCodes JSON, startedAt DATE);"
                cursor.execute(create_table_query)
                #created and updated to date-time

                create_table_query = "CREATE TABLE Regions (created TEXT, updated TEXT, id INT, name TEXT);"
                cursor.execute(create_table_query)
                #created and updatD to date-time
                #regions completed

                create_table_query = "CREATE TABLE Shops (created TEXT, updated TEXT, id TEXT, brandId TEXT," \
                                     "cityId INT, closeDate TEXT, location TEXT, phone TEXT," \
                                     "regionId INT, workHours JSON, longitude FLOAT, latitude FLOAT);"
                #completed
                cursor.execute(create_table_query)

                connection.commit()
                configParser('Config.ini', 'DataBase', 'flag_table', 'false')
                print('Table created!')
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO test_database.cities (created, updated, id, name, regionId) VALUES (%s,%s,%s,%s,%s);"
                cursor.executemany(insert_query, CitiesData)
                insert_query = "INSERT INTO test_database.regions (created, updated, id, name) VALUES (%s,%s,%s,%s);"
                cursor.executemany(insert_query, RegionsData)
                insert_query = "INSERT INTO test_database.categories (created, updated, id, name) VALUES (%s,%s,%s,%s);"
                cursor.executemany(insert_query, CategoriesData)
                insert_query = "INSERT INTO test_database.shops (created, updated, id, brandId, cityId, closeDate, location, " \
                               "phone, regionId, workHours, longitude, latitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.executemany(insert_query, ShopsData)
                insert_query = "INSERT INTO test_database.promoactions (created, updated, specialConditionsType, id," \
                               " bonusType, brandId, cashbackAmount, categoryIds, conditions, conditions_html, endedAt," \
                               " mechanicsDescription, mechanicsDescription_html, name, percent, photoSets, portalLink," \
                               " regionIds, rules_html, shopsIds, cardProgramCodes, startedAt)" \
                               " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.executemany(insert_query, PromoActionsData)
                insert_query = "INSERT INTO test_database.brands (created, updated, id, name, shortDescription, " \
                               "description, description_html, logoImages, photo, portalLink, website)" \
                               " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.executemany(insert_query, BrandsData)
                connection.commit()
                print('Inserted!')
                query = 'SELECT logoImages FROM test_database.brands'
                cursor.execute(query)
                res = cursor.fetchall()
                print(res[0])
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)