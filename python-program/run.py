# we will use mypy package to check type hinting in python
# pip install mypy

import sys 
from mypy import api as mypy_api
import subprocess

def check_type(filename:str):
    result = mypy_api.run([filename])
    # status code : 0 -> no error , 1 -> error
    stdout, stderr, status_code = result

    if stdout:
        print('Type Check Result:')
        print(stdout)

    if stderr:
        print('Errors:')
        print(stderr)
    return status_code == 0

if __name__ == "__main__":
    filename =  sys.argv[1]
    if check_type(filename):
        subprocess.run(['python', filename])
    else:
        print(f'Type check failed for {filename}')
