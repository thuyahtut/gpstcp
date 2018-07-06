#!/usr/bin/env python
from gevent.server import StreamServer
import config
import time
from logger import logger
from models import Device

def handle(sock, (clientip, clientport)):
    logger.info('New connection from %s:%s' % (clientip, clientport))
    device = None
    while True:
        data = sock.recv(config.GATEWAY_RECV_SIZE)
        if not data:
            break
        logger.info('%s > %s' % (clientip, data[:256]))
        if not device:
            try:
                '''
                    Initialize if not device and create objects
                '''
                device = Device.get_by_data(data, ipaddr=clientip)
            except Exception, e:
                logger.warning(e.message[:256])
                time.sleep(10)
                sock.close()
                return

        device.sent(data)

        resp = device.pop_response()
        while resp:
            sock.send(resp)
            logger.info('%s < %s' % (clientip, resp[:256]))
            #empty 
            resp = device.pop_response()

if __name__ == '__main__':
    server = StreamServer(
        (config.GATEWAY_HOST_LISTEN, config.GATEWAY_PORT_LISTEN),
        handle,
        spawn=config.GATEWAY_MAX_CONNECTIONS
    )
    msg = 'Gateway listening on %s:%s' % (config.GATEWAY_HOST_LISTEN, config.GATEWAY_PORT_LISTEN)
    print msg
    logger.info(msg)
    server.serve_forever()
