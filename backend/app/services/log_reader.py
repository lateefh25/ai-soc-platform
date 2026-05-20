import random
import time

sample_logs = [
    "FAILED PASSWORD from 192.168.1.10",
    "INVALID USER admin",
    "MALWARE DETECTED on HOST-22",
    "PORT SCAN DETECTED",
    "SUCCESSFUL LOGIN"
]

def stream_logs():

    while True:

        yield random.choice(sample_logs)

        time.sleep(2)