import time
def count(sec):
    for i in range(int(sec)):
        print(sec-i,end='s...')
        time.sleep(1)