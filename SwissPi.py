import textlinenetclient
import swissPiHelper
host='192.168.1.119'
port=5003


class SwissPi:
    def __init__(self):
        self.host=host
        self.port=port
        # Connect to Swiss Server
        self.client = textlinenetclient.TextLineNetClient(host, port)
        # Set up client
        self.client.sendCmd('norsp vfmts "*" dec 0 0 0 0 0 0')
        self.gpioPins=[]
        self.client.sendCmd('norsp iow %d %d' % (1,1))
        self.gpioPin=swissPiHelper.swissPiGPIOPin(self.client, 0, "led")


    def addGPIO(self,pin):
        self.gpioPins.append(swissPiHelper.swissPiGPIOPin(self.client, pin, "led"))


