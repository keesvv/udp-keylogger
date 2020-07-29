#
# Created by Kees van Voorthuizen
# GH: @keesvv
#

import socket
import sys
import time
import keyboard

PORT = 6969

def init_client(sock):
    # Bind socket
    sock.bind(("0.0.0.0", PORT))

    print("Listening...")

    # Listen for packets
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"), end="")

        # Some terminals require this
        sys.stdout.flush()

def init_server(sock, target_ip):
    keyboard.on_press(lambda event: sock.sendto(
        str.encode(event.name), (target_ip, PORT))
    )
    keyboard.wait()

# Create UDP socket
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

if len(sys.argv) > 1:
    init_server(sock, sys.argv[1])
else:
    init_client(sock)
