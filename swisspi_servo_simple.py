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
#client.sendCmd('norsp svcw 0 118 515 1000')
client.sendCmd('norsp svcw 1 122 520 0')

# Enable servo mode
client.sendCmd('norsp svme')

# Move motors
client.sendCmd('norsp svmv 0 250 0 0')
client.sendCmd('norsp svmv 1 400 0 0')
client.commit()
