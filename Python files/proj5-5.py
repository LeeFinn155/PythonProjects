# Simple TCP Server

import socket

master_socket = socket.socket() # Defaults to TCP

master_socket.bind(("",12345)) # IP (of interfaces), TCP port

master_socket.listen(5) # Start listening for connections
                        # (The number is the "backlog")

# Loop forever
while True:
    # Wait for a connection request, send them data, close, repeat
    print("Waiting for a connection...")
    (one_connection, remote_addr) = master_socket.accept()

    # We now have a new socket, and info on where the socket is from

    (host, port)= remote_addr  # "Decode" the tuple

    print("Connection from host,", host," and TCP port", port)

    # Send them something "interesting"
    b_str = "Hello from Lee!!!\n"

    one_connection.sendall(b_str)

    # Now let them end
    one_connection.close()
