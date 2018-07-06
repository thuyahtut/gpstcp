import re
import config
from .adapter import Adapter
from models import Message

class concox(Adapter):

    @classmethod
    def decode(cls, datastring):
        re_login = '^##,imei:(?P<imei>\d{15}),A'
        re_heartbeat = '^heardbeat'

        if re.match(re_login, datastring):
            #check datastring
            #imei = re.match(re_init, datastring).group('imei')
            #message = Message(imei=imei, message_type=config.MESSAGE_TYPE_INIT, message_datastring=datastring)

        elif re.match(re_location,datastring):
            #check datastring
            #match = re.match(re_location_full, datastring)
            #imei = match.group('imei')
            #message = Message(imei=imei, message_type=config.MESSAGE_TYPE_LOCATION_FULL, message_datastring=datastring)