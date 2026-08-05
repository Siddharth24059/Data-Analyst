# wap in python to select data from mysql database 
import sys 
from pdbc.db_config import getConnection

def getAllUserData():
    conn = getConnection()
    # Make the cursor Object 
    cursor = conn.cursor()
    cursor.execute("select * from users")
    result_set = cursor.fetchall()
    return result_set
    
def main():
    userdata = getAllUserData()
    for id,name,age in userdata:
        print(f'id={id} name={name} age={age}')
        print('===================================')


if __name__ == '__main__':
    sys.exit(main())