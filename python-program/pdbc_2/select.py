import sys

def selectAllProduct():
    from db2 import getConnection # lazy import
    try:
        conn=getConnection()
        cursor=conn.cursor()
        query= f"select * from products"
        cursor.execute(query)
    except Exception as e:
        print(f'Query Error {e}')
    finally:
        resultSet = cursor.fetchall()
        conn.close()
    return resultSet
def main():
    result = selectAllProduct()
    for row in result:
        id,name,desc,price,brand,qty = row
        print(f'id={id}, name={name}, desc ={desc},brand={brand},price={price},qty={qty}')
        print("=========================================================================")
        
        
if __name__=="__main__":
    sys.exit(main())
