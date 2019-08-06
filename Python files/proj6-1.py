# Small program tos end data to a Graphite server

import socket
import time

sock = socket.socket()      # A TCP socket

sock.connect(( "172.22.80.39", 2003))    # Graphite's ingress port

#       Graphite Data Format:
#
# DataPointName Value WhenItHappened
#
#   if WhenItHappened = -1 --> "NOW"

val = 1

while (True):
    line = " itt385.finn.stupidData" + str(val) + " -1\n"

    # Convert to bytes() and transmit it
    line = line.encode("utf-8")
    sock.send( line )

    val = val + 1
    if (val > 100):
        val = 1
    time.sleep(10)

# Done
sock.close()
