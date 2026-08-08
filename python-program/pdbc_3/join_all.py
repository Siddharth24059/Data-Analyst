from db import getConnection

def join_all():
    try:
        conn = getConnection()
        cursor = conn.cursor()

        query = """
        SELECT 
            u.user_id,
            u.user_name,
            u.user_age,
            b.bus_name,
            b.source,
            b.destination
        FROM users u
        JOIN buses b ON u.user_id = b.bus_id
        """

        cursor.execute(query)
        data = cursor.fetchall()

        for row in data:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


join_all()