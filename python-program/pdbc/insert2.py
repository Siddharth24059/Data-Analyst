from pdbc.db_config import getConnection
import sys 
def insertUser(name,age):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = f"Insert into users(name,age) values('{name}','{age}')"
        cursor.execute(query)
    except Exception as e:
        print(f' Error in Query : {e}')
    finally:
        conn.commit()
        conn.close()
        return cursor._last_insert_id

def main():
    name = input('Enter the name:')
    age = input('Enter the age:')
    user_id = insertUser(name,age)
    if user_id:
        print('User Inserted with ID=',user_id)
    else:
        print('User Not Inserted')

if __name__ == '__main__':
    sys.exit(main())