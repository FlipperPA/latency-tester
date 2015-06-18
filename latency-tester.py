import sys, pexpect, time, datetime

# SET YOUR PING INTERVAL HERE, IN SECONDS
interval = 5

# LOG TO WRITE TO WHEN PINGS TAKE LONGER THAN THE THRESHOLD SET ABOVE
i = datetime.datetime.now()
log_file = 'latency-tester.' + i.strftime('%Y.%m.%d.%H.%M.%S') + '.log'

# SET YOUR PING RESPONSE TIME THRESHOLD HERE, IN MILLISECONDS
threshold = 250

# WHO SHOULD WE RUN THE PING TEST AGAINST
ping_destination = 'www.google.com'

def write_to_file(file_to_write, message):
    fh = open(file_to_write, 'a')
    fh.write(message)
    fh.close()

count = 0
line = 'Ping Interval: ' + str(interval) + ', Destination: ' + ping_destination + ', Threshold to Log (msec): ' + str(threshold) + '\n'

write_to_file(log_file, line)
         
ping_command = 'ping -i ' + str(interval) + ' ' + ping_destination
print(line)

child = pexpect.spawn(ping_command)
child.timeout=1200

while 1:
    line = child.readline()
    if not line:
        break

    if line.startswith(b'ping: unknown host'):
        print('Unknown host: ' + ping_destination)
        write_to_file(log_file, 'Unknown host: ' + ping_destination)
        break

    if count > 0:
        ping_time = float(line[line.find(b'time=') + 5:line.find(b' ms')])
        line = time.strftime("%m/%d/%Y %H:%M:%S") + ": " + str(ping_time)
        print(str(count) + ": " + line)

        if ping_time > threshold:
            write_to_file(log_file, line + '\n')

    count += 1
