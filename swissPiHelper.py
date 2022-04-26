import textlinenetclient

class swissPiGPIOPin:
    def __init__(self,SwissPiClient, pin,use):
        self.pin=pin
        self.use=use
        self.SwissPiClient=SwissPiClient

    def writeTrue(self):
        self.SwissPiClient.sendCmd('norsp iow %d %d' % (self.pin,1))



