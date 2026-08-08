from db import getConnection

def get_users():
    try:
        conn = getConnection()
        cursor = conn.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()


get_users()