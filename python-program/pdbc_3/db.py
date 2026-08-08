import mysql.connector

DB_CREDS = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'user_bus'   # 
}

def getConnection(debug=False):
    try:
        conn = mysql.connector.connect(**DB_CREDS)

        if conn.is_connected():
            if debug:
                print("Database is connected successfully")
            return conn
        else:
            print("Error in connection")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None