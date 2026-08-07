import mysql.connector 
import sys  # db object> connection object >cursor object we can access by it 

DB_CRED = {
    "host": "127.0.0.1",
    "port": '3306',
    "user": "root",
    "password": "",
    "database": "sipher_db"
}

def getConnection():
    try:
     conn = mysql.connector.connect(**DB_CRED)
     if conn.is_connected():
        print('Database connected successfully')
        return conn
     else:
        print('connection error')
    except Exception as e:
        print(f' Database Error :{e}')
    return None
    
def main():
     result = getConnection()
     print('Result:',result)
     
if __name__ == '__main__':
    sys.exit(main())      