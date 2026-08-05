# ctrl+shift+p
# select interprete: select your myenv python.exe recommended

# package -> subpackage

# mysql: package-> connector

import mysql.connector

DB_CREDS = {
    "host": "127.0.0.1",
    "port": '3306',
    "user": "root",
    "password": "",
    "database": "sipher_db"
}


def getConnection(debug=False):
    try:
        conn = mysql.connector.connect(**DB_CREDS)
        if conn.is_connected():
            if debug == True:
                print("Database connection successful")
            return conn
        else:
            print('Error in connection')
            return None
    except Exception as e:
        print(f' Eerror :{e}') 
        return None
          