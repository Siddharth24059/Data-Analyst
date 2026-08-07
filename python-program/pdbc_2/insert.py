from db2 import getConnection
import sys

def insertProduct(name,desc,price,brand,qty):
    try:
        conn=getConnection()
        cursor=conn.cursor()
        query= f"insert into products(`name`,`desc`,`price`,`brand`,`qty`) values ('{name}','{desc}','{price}','{brand}','{qty}')"
        cursor.execute(query)
    except Exception as e:
        print(f'Query Error {e}')
    finally:
        conn.commit()
        conn.close()
    return cursor.lastrowid
def main():
    name = input('Enter ther name:')
    desc = input('Enter ther description:')
    price  = input('Enter ther price:')    
    brand = input('Enter ther brand:')
    qty = input('Enter ther qty:')
    insertProduct(name,desc,price,brand,qty)
    
        
if __name__=="__main__":
    sys.exit(main())