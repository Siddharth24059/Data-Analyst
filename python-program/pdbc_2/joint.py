import sys

def selectAllProduct():
    from db2 import getConnection # lazy import
    try:
        conn=getConnection()
        cursor=conn.cursor()
        query= f"select u.id as users_id,u.name as users_name, u.age as users_age, p.id as products_id,p.name as products_name, p.`desc` as products_description, p.price as products_price, p.brand as products_brand,p.qty as products_qty FROM products as p CROSS JOIN users as u;"
        print(query)
        cursor.execute(query)
    except Exception as e:
        print(f'Query Error {e}')
    finally:
        resultSet = cursor.fetchall()
        conn.close()
    return resultSet
def main():
    result = selectAllProduct()
    i=0
    for row in result:
        (users_id, users_name, users_age, products_id, products_name, products_description,products_price, products_brand, products_qty) = row
        print(f'users_id = {users_id},users_name={users_name},users_age={users_age}')
        print(f'products_id={products_id}, products_name={products_name}, products_description={products_description}, products_brand={products_brand}, products_price={products_price}, products_qty={products_qty}')
        print("================================")
        i=i+1
        
if __name__=="__main__":
    sys.exit(main())