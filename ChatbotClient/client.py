import socket

HEADER = 512
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

print("Connected! Use only keywords for more accurate answers.")
while True:
    msg = input()
    if msg:
        send_message(msg)
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length:
        print(msg_length)
