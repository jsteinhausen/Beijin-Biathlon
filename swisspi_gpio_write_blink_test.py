import time
import textlinenetclient

# Host and port of Swiss Server. Change as needed e.g. host '192.168.1.110'.
host = '192.168.1.20'
port = 5003

# Connect to Swiss Server
client = textlinenetclient.TextLineNetClient(host,port)

# Set up client
client.sendCmd('norsp vfmts "*" dec 0 0 0 0 0 0')

# Parameters
pin = 8  # GPIO pin (0..15)
output = 1  # Output state (0 or 1)

while True:
    # Write output state of GPIO pin
    client.sendCmd('norsp iow %d %d' % (pin,1))

    # Read output state of GPIO pin
    client.sendCmd('ior %d' % pin,True)
    tokens = client.tokenizeLine(client.rcvRsp())
    print("GPIO pin %d: output state %d" % (pin,int(tokens[3])))
    time.sleep(2)

    # Write output state of GPIO pin
    client.sendCmd('norsp iow %d %d' % (pin, 0))

    # Read output state of GPIO pin
    client.sendCmd('ior %d' % pin, True)
    tokens = client.tokenizeLine(client.rcvRsp())
    print("GPIO pin %d: output state %d" % (pin, int(tokens[3])))
    time.sleep(2)
