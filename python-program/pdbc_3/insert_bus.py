from db import getConnection
import sys

def insert_data(name, source, destination):
    conn = None
    cursor = None

    try:
        conn = getConnection()

        if conn is None:
            print(" DB connection failed")
            return None

        cursor = conn.cursor()

        query = "INSERT INTO buses(bus_name, source, destination) VALUES(%s, %s, %s)"
        cursor.execute(query, (name, source, destination))

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
    name = input("Enter the Bus name: ")
    source = input("Enter the Source: ")
    destination = input("Enter the destination: ")

    data = insert_data(name, source, destination)

    if data:
        print(" Bus Inserted:", data)
    else:
        print(" Not Inserted")


if __name__ == "__main__":
    sys.exit(main())