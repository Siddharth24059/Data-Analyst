from db2 import getConnection
import sys

def updateProduct(id,name,desc,price,brand,qty):
    try:
        conn=getConnection()
        cursor=conn.cursor()
        query= f"update products set name='{name}',`desc`='{desc}',price='{price}', brand='{brand}', qty='{qty}' where id='{id}'"; 
        cursor.execute(query)
    except Exception as e:
        print(f'Query Error {e}')
    finally:
        conn.commit()
        conn.close()
    return cursor.rowcount
def main():
    result = updateProduct('1','Harpik','This is Harpik','60','Harpik','100')
    if result:
        print('record updated')
    else:
        print('record not updated')                           
    
        
if __name__=="__main__":
    sys.exit(main())
