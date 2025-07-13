from datetime import datetime
import time

if __name__ == "__main__":
    
    MAX_LOOP = 1000
    INTERVAL = 900 #15 minutes

    i = 0
    while i<=MAX_LOOP:
        print(datetime.now())
        time.sleep(INTERVAL)
        i+=1