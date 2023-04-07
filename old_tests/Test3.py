# import socket

# client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_server.connect(("localhost", 5001))
# while True:
#     message = input("Wrtie text: ")
#     client_server.send(message.encode())
#     info = client_server.recv(4096)
#     print(info)

class One():
    def __init__(self) -> None:
        "Some text"
        self.aa = 4
    # def print_shit(self):
    #     print("Shit")

class Two():
    def __init__(self) -> None:
        self.obj_one = 1

class Three():
    def __init__(self) -> None:
        self.obj_three = 5

from abc import ABCMeta, abstractmethod, ABC

class IInterface(ABC):
    @abstractmethod
    def create_one(self) -> One:
        "Some text"
        ...
    @abstractmethod
    def create_two(self) -> Two:
        ...
    @abstractmethod
    def create_three(self) -> Three:
        ...

    @abstractmethod
    def print_shit(self, text):
        print(text)

class Test(IInterface, Two, Three):
    def __init__(self) -> None:
        super().__init__()
        ...
    
    def create_one(self) -> One:
        return super().create_one()
    
    def create_two(self) -> Two:
        return super().create_two()
    
    def create_three(self) -> Three:
        return super().create_three()
    
    def print_shit(self):
        print("tre")
        return super().print_shit("allah")


obj = Test()
obj.print_shit()

print(obj.obj_one)

price =  int(5)
print(price)
