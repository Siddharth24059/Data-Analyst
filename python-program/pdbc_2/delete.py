from db2 import getConnection
import sys

def deleteProduct(id):
    try:
        conn=getConnection()
        cursor=conn.cursor()
        query= f"delete from products where id='{id})'"
        cursor.execute(query)
    except Exception as e:
        print(f'Query Error {e}')
    finally:
        conn.commit()
        conn.close()
    return cursor.rowcount
def main():
    id = 3
    result = deleteProduct(id)
    if result:
        print(f' record deleted for ID = {id}')
    else:
        print('record not deleted')      
    
        
if __name__=="__main__":
    sys.exit(main())