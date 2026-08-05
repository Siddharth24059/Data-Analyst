from pdbc.db_config import getConnection
import sys 

def DeleteUser(id):
    conn = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id=%s"
        cursor.execute(query, (id,))
        return cursor.rowcount
    except Exception as e:
        print(f'Error in Query: {e}')
        return 0
    finally:
        if conn:
            conn.commit()
            conn.close()

def main():
    id = input('Enter the ID:')

    effectedRows = DeleteUser(id)
    if effectedRows:
        print('User Deleted with ID =', id)
    else:
        print('User Not Deleted')

if __name__ == '__main__':
    sys.exit(main())