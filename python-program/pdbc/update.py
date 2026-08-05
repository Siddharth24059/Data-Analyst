from pdbc.db_config import getConnection
import sys 

def UpdatetUser(name,age,id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        query = f"update users set name='{name}',age='{age}' where id='{id}'"
        cursor.execute(query)
    except Exception as e:
        print(f' Error in Query : {e}')
    finally:
        conn.commit()
        conn.close()
        return cursor._rowcount

def main():
    
    id =  input('Enter the ID:')
    name = input('Enter the name:')
    age = input('Enter the age:')

    effectedRows = UpdatetUser(name,age,id)
    if effectedRows:
        print('User Updated with ID=',id)
    else:
        print('User Not Updated')

if __name__ == '__main__':
    sys.exit(main())