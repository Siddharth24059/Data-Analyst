from db import getConnection
import sys

def insert_cities(city_name):
    conn = None
    cursor = None

    try:
        conn = getConnection()

        if conn is None:
            print(" DB connection failed")
            return None

        cursor = conn.cursor()

        query = "INSERT INTO cities(city_name) VALUES(%s)"
        cursor.execute(query, (city_name,))

        conn.commit()
        return cursor.lastrowid

    except Exception as e:
        print(f"Error in Query: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def main():
    city_name = input("Enter City Name: ")

    data = insert_cities(city_name)

    if data:
        print(" City Inserted:", data)
    else:
        print(" Not Inserted")


if __name__ == "__main__":
    sys.exit(main())