from db import getConnection

def get_cities():
    try:
        conn = getConnection()
        cursor = conn.cursor()

        query = "SELECT * FROM cities"
        cursor.execute(query)

        data = cursor.fetchall()

        for row in data:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()


get_cities()