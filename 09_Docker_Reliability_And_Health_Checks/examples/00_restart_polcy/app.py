import os
import sys
import time
from datetime import datetime

if __name__ == "__main__":
    print("Strating proccesing app!!")
    counter = 1
    MAX_COUNTER = int(os.getenv("MAX_COUNTER", 60))
    while True:
        time.sleep(1)  # simulate work
        timestamp = datetime.now()
        print(f"[{timestamp}] {counter}/{MAX_COUNTER} - Working!")
        counter += 1
        if counter >= MAX_COUNTER:
            sys.exit(0)
            raise ValueError
