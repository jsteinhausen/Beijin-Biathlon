import textlinenetclient

# Host and port of Swiss Server. Change as needed e.g. host '192.168.1.110'.
host = 'localhost'
port = 5003

# Connect to Swiss Server
client = textlinenetclient.TextLineNetClient(host,port)

# Set up client
client.sendCmd('norsp vfmts "*" dec 0 0 0 0 0 0')

# Make sure servo mode is disabled
client.sendCmd('norsp svmd')

# Set PWM frequency of 50 Hz
client.sendCmd('norsp ppw 121')

# Set up servo channels
client.sendCmd('norsp svcw 0 118 515 1000')
client.sendCmd('norsp svcw 1 122 520 0')

# Servo motors should be set into a valid position at some point. Two methods:
# (a) Before svme: set a PWM pulse width that's a range specified in svcw.
# (b) After svme: move position without timings i.e. parameters 3 and 4 set to zero.

# (a)
# Set PWM pulse width of channels in valid range before svme in case you want
# the first movement use a period (svmv parameter 3 non-zero).
#client.sendCmd('norsp pcw  0 1  0 0 0 316')
#client.sendCmd('norsp pcw  1 1  0 0 0 200')

# Enable servo mode
client.sendCmd('norsp svme')

# (b)
# Set PWM pulse width of channels in valid range
client.sendCmd('norsp svmv 0 250 0 0')
client.sendCmd('norsp svmv 1 200 0 0')

# Engage motor movements, wait for completion
client.sendCmd('norsp svmv 0 750 2000 500')
client.sendCmd('      svmv 0 250 2000 3000')
client.sendCmd('norsp svmv 1 400 1550 500')
client.sendCmd('      svmv 1 200 1550 3000')
client.commit()
client.rcvRsp()
client.rcvRsp()

# Disable servo mode, wait for completion
client.sendCmd('svmd',True)
client.rcvRsp()
