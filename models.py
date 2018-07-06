class Device:
    '''
        initialize and defination of device
    '''
    def __init__(self,param):
        self.something = param

    #imei =
    adapter = None
    responses =
    @classmethod
    def get_by_data(cls,datastring):
        #login datapacket
        '''
            create device definiation ORM
        '''
        adapter = Adapter.detect(datastring)
        if not adapter:
            raise Exception("Couldn't determine adapter from datastring: %s" % datastring)
        
        message = adapter.decode(datastring)

        if not message.imei:
            raise Exception("Couldn't get imei from datastring: %s" % datastring)

        """ Try retrieving device from db
           check exist or not, login
        """
        try:
            #device = 
        except Exception:

        return device

    def pop_response(self):
        """ Get the current response, and messages waiting
        """
        try:
            return self.responses.pop(0)
        except IndexError:
            return None

    def sent(self, datastring):
        if not self.adapter:
            self.adapter = Adapter.detect(datastring)
        if not self.adapter:
            raise Exception("Coudln't determine adapter from datastring: %s" % datastring)

        #decode 
        #save process
        # filter

        response = self.adapter.response_to(message)
        if response:
            self.response.append(response)
