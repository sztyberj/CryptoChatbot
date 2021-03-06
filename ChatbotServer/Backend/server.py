import socket
import threading
import sys
sys.path.append(r'C:\Users\sztyb\PycharmProjects\ChatBot')
import ChatbotServer.Backend.scrapper
import ChatbotServer.Backend.api
import ChatbotServer.Database.database as db
from ChatbotServer.Backend import chatbot



New = db.Database()

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            s_mess = chatbot.talk(msg)

            if msg in chatbot.user_bye:
                connected = False

            print(f"[{addr}] {msg}")
            output = s_mess.encode(FORMAT)
            print(output)
            conn.send(output)

    conn.close()
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("[STARTING] Server is starting...")
start_server()