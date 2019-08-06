# Simple TCP Client

import socket

my_socket = socket.socket() # Defaults to TCP

my_socket.connect(("172.22.80.39", 17)) #Note the 2 parens to create the tuple

# Or could do in 2-steps
#
# remote_host = ("172.22.80.19", 17)  # IP,port tuple
# my_socket.connect(remote_host)
#


# In this case, sending data is not needed
data = my_socket.recv(1024)     # Gets up to 1024 "bytes" of data
all_data = b""

while(len(data) > 0):
      all_data = all_data + data    # Cocatenate the chunk received to
                                    # the end of the "whole" buffer

      data = my_socket.recv(1024)   # Get the next chunk of data

# Convert bytes() into str()
all_data = all_data.decode('utf-8')

print(all_data)

my_socket.close()
