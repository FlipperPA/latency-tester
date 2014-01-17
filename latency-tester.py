import pexpect, time, sys

# SET YOUR PING INTERVAL HERE, IN SECONDS
interval = 5

# LOG TO WRITE TO WHEN PINGS TAKE LONGER THAN THE THRESHOLD SET ABOVE
log_file = 'latency-tester.log'

# SET YOUR PING RESPONSE TIME THRESHOLD HERE, IN MILLISECONDS
threshold = 100

# WHO SHOULD WE RUN THE PING TEST AGAINST
ping_destination = 'www.google.com'

count = 0
line = 'Ping Interval: ' + str(interval) + ', Destination: ' + ping_destination + ', Threshold to Log (msec): ' + str(threshold) + '\n'

fh = open(log_file, 'w+')
fh.write(line)
fh.close()
         
ping_command = 'ping -i ' + str(interval) + ' ' + ping_destination
print line

child = pexpect.spawn(ping_command, timeout=(interval + 30))

while 1:
    count += 1
    line = child.readline()
    if not line: break

    if count > 1:
        ping_time = float(line[line.find('time=') + 5:line.find(' ms')])
        line = time.strftime("%m/%d/%Y %H:%M:%S") + ": " + str(ping_time)
        print line

        if ping_time > threshold:
            fh = open(log_file, 'a')
            fh.write(line + '\n')
            fh.close()
