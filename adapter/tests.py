from concox import concox
heartbeat = 'heartbeat hexdata'
location = 'locationdata'

def test_location():
    message = concox.decode(location)
    assert(message)

'''
do another testing
'''