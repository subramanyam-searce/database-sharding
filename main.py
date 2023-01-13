import psycopg2
import json

f = open("config.json")
data = json.load(f)
user_country_a_k = data["user_country_a_k"]
user_country_l_z = data["user_country_l_z"]

conn = None

def getDBConnection(connection_string):
    global conn
    conn = psycopg2.connect(connection_string)
    return conn.cursor()

def insertData(name, date_of_birth, gender, age, country):
    db_connection_string = ""
    
    country_ascii = ord(country[0].lower())
    if country_ascii < 97 or country_ascii > 122:
        return "Country name should start with a valid letter"
    elif country_ascii >= 97 and country_ascii <= 107:
        db_connection_string = user_country_a_k
    elif country_ascii >= 108 and country_ascii <= 122:
        db_connection_string = user_country_l_z
    
    cursor = getDBConnection(db_connection_string)
    query="INSERT INTO app_user(name, date_of_birth, gender, age, country) VALUES(%s, %s, %s, %s, %s);"
    cursor.execute(query, vars=(name, date_of_birth, gender, age, country))

    count = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return (count, "Record inserted successfully into mobile table")


for row in data["data"]:
    print(insertData(row[0], row[1], row[2], row[3], row[4]))