import os
import signal
import sys
import time
from datetime import datetime


def signal_handler(signum, frame):
    print(f"Gracefully shutting down after receiving signal {signum}")
    sys.exit(0)
    

if __name__ == "__main__":
    print("Strating proccesing app!!")
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    counter = 1
    MAX_COUNTER = int(os.getenv("MAX_COUNT", 60))
    while True:
        time.sleep(1)  # simulate work
        timestamp = datetime.now()
        print(f"[{timestamp}] {counter}/{MAX_COUNTER} - Working!")
        counter += 1
        if counter >= MAX_COUNTER:
            raise ValueError
