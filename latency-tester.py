import datetime
import os
from time import sleep

from ping3 import ping

# SET YOUR PING RESPONSE TIME THRESHOLD HERE, IN SECONDS
THRESHOLD = 0.25  # 250 milliseconds is the Comcast SLA threshold.

# SET YOUR PING INTERVAL HERE, IN SECONDS
INTERVAL = 1

# WHO SHOULD WE RUN THE PING TEST AGAINST
DESTINATION = "www.google.com"

# LOG TO WRITE TO WHEN PINGS TAKE LONGER THAN THE THRESHOLD SET ABOVE
i = datetime.datetime.now()
log_file = "logs/latency-tester." + i.strftime("%Y.%m.%d.%H.%M.%S") + ".log"


def write_to_file(file_to_write, message):
    os.makedirs(os.path.dirname(file_to_write), exist_ok=True)
    fh = open(file_to_write, "a")
    fh.write(message + "\n")
    fh.close()


count = 0
header = f"Pinging {DESTINATION} every {INTERVAL} secs; threshold: {THRESHOLD} secs."
print(header)
write_to_file(log_file, header)

while True:
    count += 1
    latency = ping(DESTINATION)

    # Do we want to write it to the log?
    if latency is None or latency > THRESHOLD:
        write_log = "Yes"
    else:
        write_log = "No"

    # Use better text is packet is dropped
    if latency is None:
        latency_text = "PACKET DROPPED"
    else:
        latency_text = f"{latency} secs"

    line = f"Pinged {DESTINATION}; latency: {latency_text}; logging: {write_log}"
    print(line)

    if write_log == "Yes":
        write_to_file(log_file, line)
    sleep(INTERVAL)
