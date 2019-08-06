import socket

sock = socket.socket(type=socket.SOCK_DGRAM) # Ask for a UDP Socket

# We are going to use broadcasts, so we have to do an extra step
sock.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Need to set our port, in this case UDP Port 12345 (on all interfaces)
sock.bind( ("", 12345) )


# Get ready to transmit something
line = "Hello from Lee\n"
line = line.encode('utf-8')

# Send it
#   to host 255.255.255.255 and UDP port 12345
#   (aka to all hosts and all interfaces)
sock.sendto( line, ("255.255.255.255", 12345) )

# Now wait for others to transmit some data to me
while (True):
    # Big recieve buffer, effectively saying how much data willing to accept
    (data, addr) = sock.recvfrom(10240)

    # Data will be in bytes(), so convert it tinto str()
    data = data.decode('utf-8')

    print( str(addr), "said", data)


#   Close never reached (infinite loop)
sock.close()
