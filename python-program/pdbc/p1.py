from pdbc.db_config import getConnection

import sys

def main():
    conn =   getConnection()
    print(conn)
   
    
if __name__ == "__main__":
    sys.exit(main())    
        