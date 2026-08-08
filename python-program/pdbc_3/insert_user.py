from db import getConnection
import sys

def insert_user(user_name, user_age):
    conn = None
    cursor = None

    try:
        conn = getConnection()

        if conn is None:
            print(" DB connection failed")
            return None

        cursor = conn.cursor()

        query = "INSERT INTO users(user_name, user_age) VALUES(%s, %s)"
        cursor.execute(query, (user_name, user_age))

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
    user_name = input("Enter User Name: ")
    user_age = int(input("Enter User Age: "))

    data = insert_user(user_name, user_age)

    if data:
        print(" User Inserted:", data)
    else:
        print(" Not Inserted")


if __name__ == "__main__":
    sys.exit(main())