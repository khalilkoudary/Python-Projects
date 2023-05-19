import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    """ Connecting to the server. """
    client.connect(ADDR)


    ##receiving menu from server
    msg = client.recv(SIZE).decode(FORMAT)
    number = input(f"{msg}")

      ##sending selection to server
    client.send(number.encode(FORMAT))
    if(number =="1"):
        msg = client.recv(SIZE).decode(FORMAT)
        name = input(f"{msg}")
        client.send(name.encode(FORMAT))
        msg=client.recv(SIZE).decode(FORMAT)
        print(f"{msg}")

    elif number =="2":
        msg = client.recv(SIZE).decode(FORMAT)
        name = input(f"{msg}")
        ##if customer leaves name field empty (null) or whitespaced
        while not any(name):
            name=input("Customer name cannot be empty.\nEnter customer name:")
        while name.isspace():
            name = input("Customer name cannot be empty.\nEnter customer name:")
        client.send(name.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        age = input(f"{msg}")
        client.send(age.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        address = input(f"{msg}")
        client.send(address.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        telephone = input(f"{msg}")
        client.send(telephone.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"{msg}")

    elif number == "3":
        msg = client.recv(SIZE).decode(FORMAT)
        name = input(f"{msg}")
        while not any(name):
            name=input("Customer name cannot be empty.\nEnter customer name:")
        while name.isspace():
            name = input("Customer name cannot be empty.\nEnter customer name:")
        client.send(name.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        age = input(f"{msg}")
        client.send(age.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        address = input(f"{msg}")
        client.send(address.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        telephone = input(f"{msg}")
        client.send(telephone.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"{msg}")
    elif number =="4":
        msg = client.recv(SIZE).decode(FORMAT)
        name = input(f"{msg}")
        while not any(name):
            name=input("Customer name cannot be empty.\nEnter customer name:")
        while name.isspace():
            name = input("Customer name cannot be empty.\nEnter customer name:")
        client.send(name.encode(FORMAT))
        exists = client.recv(SIZE).decode(FORMAT)
        if(exists =="1"):
          msg=client.recv(SIZE).decode(FORMAT)
          field = input(f"{msg}")
          client.send(field.encode(FORMAT))
          msg=client.recv(SIZE).decode(FORMAT)
          updatedInfo = input(f"{msg}")
          client.send(updatedInfo.encode(FORMAT))
          msg=client.recv(SIZE).decode(FORMAT)
          print(f"{msg}")
        else:
            print("Customer name not in database")
    elif number == "5":
        print("** Python DB contents **")
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"{msg}")
    elif number =="6":
        print("Goodbye!")
        client.close()




    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()