# import asyncio
# import time

# async def say_after(seconds, text):
#         while True:
#             print(text) 
#             await asyncio.sleep(seconds)    


# async def main(text):
#     task1 =  asyncio.create_task(say_after(3, "One"))
#     task2 = asyncio.create_task(say_after(2, "tree"))
#     cort = task1.get_coro()
#     await asyncio.gather(task1, task2)

#     # await task1
#     # await task2

# asyncio.run(main("Hello"))

import socket
from select import select

to_monitor = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5001))
server_socket.listen()


def accept_connection(server_socket):
        client_socker, addr = server_socket.accept()
        print("Connect from:", addr)
        to_monitor.append(client_socker)

def send_message(client_socker):
        request = client_socker.recv(4096)
        if request:
            response = "Hello bro!".encode()
            client_socker.send(response)
        else:     
            client_socker.close()

def event_loop():
    while True:
        ready_for_read, _, _, = select(to_monitor, [], [])
        for sock in ready_for_read:
            if sock is server_socket:
                  accept_connection(sock)
            else:
                send_message(sock)

if __name__ == "__main__":
    to_monitor.append(server_socket)
    accept_connection(server_socket)
    event_loop()
