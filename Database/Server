import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
repeat = True

##opening the file containing the database
file = open("data.txt", "r")

##loading the database into a 2d list called customerListUnclean (because whitespace might exist)
readList = file.readlines()
customerListUnclean = []
for line in readList:
  line = line.rstrip('\n')
  custData = line.split('|')
  customerListUnclean.append(custData)

##Cleaning the 2d list
customerList =[]
for l1 in customerListUnclean:
    l1clean=[]
    for l2 in l1:
        l1clean.append(l2.strip())
    customerList.append(l1clean)

##making sure that name is present. If not, customer record is deleted
k=0
while k<len(customerList):
    if not any(customerList[k][0]):
        del (customerList[k])
    k=k+1

##making sure that no duplicate names are present in the origianl database. Delete if any found
for i in range(len(customerList)):
    if i==len(customerList)-1:
        break
    for j in range(i+1, len(customerList)):
        if j==len(customerList):
            break
        if customerList[i][0]==customerList[j][0]:
            del(customerList[j])


def main():

    ##connecting server to client
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    while repeat:
        """ Server is listening, i.e., server is now waiting for the client to connected. """
        server.listen()
        print("[LISTENING] Server is listening.")
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

##sending menu to client
## I decided to give the client 6 options instead of 8. option 4 combines what options 4, 5, & 6 (provided in the assignment description) do
        menu = '''
        Python DB Menu
        1. Find customer
        2. Add customer
        3. Delete customer
        4. Update customer information
        5. Print report
        6. Exit 
        Select:
        '''

        conn.send(menu.encode(FORMAT))

        #

        choice = conn.recv(SIZE).decode(FORMAT)

        ##handling of client's selection

        ##if client selects 5 from the menu, the report will be printed
        if choice == "5":
            customerList.sort()
            for i in range(len(customerList)):
                if customerList[i][0].isspace():
                    del(customerList[i])
                elif customerList[i][0]:
                    continue
                else:
                    del (customerList[i])
            database = ""
            for i in range(len(customerList)):
                for j in range(len(customerList[i])):
                    if j==3:
                        database +=customerList[i][j]
                    else:
                        database += customerList[i][j] +"|"
                database += "\n"
            conn.send(database.encode(FORMAT))
        ##if client selects 1 from the menu, the server will ask the client for the name of the customer.
        ##if name exists in the database, customer information will be sent to client.
        ##if not, client will be notified that the customer does not exist
        elif choice == "1":
            found = True
            conn.send("Customer name:".encode(FORMAT))
            name = conn.recv(SIZE).decode(FORMAT)
            n = 0
            for i in range(len(customerList)):
                if (customerList[i][0].strip() == name):
                    found = True
                    n = i
                    break
                else:
                    found = False
            if found:
                nameFound = "Server response: " + str(customerList[n])
                conn.send(nameFound.encode(FORMAT))
            else:
                nameNotFound = "Server response: " + name + " not in database"
                conn.send(nameNotFound.encode(FORMAT))
        ##if client selects 2, they get prompted to insert the information for a new customer they want to add

        elif choice == "2":
            conn.send("Customer name:".encode(FORMAT))
            name = conn.recv(SIZE).decode(FORMAT)
            conn.send("Customer age:".encode(FORMAT))
            age = conn.recv(SIZE).decode(FORMAT)
            conn.send("Customer address:".encode(FORMAT))
            address = conn.recv(SIZE).decode(FORMAT)
            conn.send("Telephone number:".encode(FORMAT))
            telephone = conn.recv(SIZE).decode(FORMAT)
            customerList.append([name, age, address, telephone])
            exists = False
            n=len(customerList)-1
            for i in range(len(customerList)):
                j=len(customerList)-1
                if i == j:
                    break
                if customerList[i][0]==customerList[j][0]:
                    exists = True
            if exists:
                conn.send("Customer with similar name already exists".encode(FORMAT))
                del(customerList[n])
            else:
                conn.send("New customer added".encode(FORMAT))

        ##if client selects option 3, they get prompted to enter the information

        elif choice == "3":
            conn.send("Enter information of customer you want to delete:\nCustomer name:".encode(FORMAT))
            name = conn.recv(SIZE).decode(FORMAT)
            conn.send("Customer age:".encode(FORMAT))
            age = conn.recv(SIZE).decode(FORMAT)
            conn.send("Customer address:".encode(FORMAT))
            address = conn.recv(SIZE).decode(FORMAT)
            conn.send("Telephone number:".encode(FORMAT))
            telephone = conn.recv(SIZE).decode(FORMAT)
            if [name, age, address, telephone] in customerList:
                customerList.remove([name, age, address, telephone])
                conn.send("Customer removed from database".encode(FORMAT))
            else:
                conn.send("Customer does not exist in database".encode(FORMAT))

        ##this is updating the list
        elif choice == "4":
            found = True
            conn.send("Enter the name of customer whose information you want to update:".encode(FORMAT))
            name = conn.recv(SIZE).decode(FORMAT)
            n = 0
            for i in range(len(customerList)):
                if (customerList[i][0].strip() == name):
                    found = True
                    n = i
                    break
                else:
                    found = False
            if found:
                conn.send("1".encode(FORMAT))
                conn.send("Which field would you like to update?".encode(FORMAT))
                field = conn.recv(SIZE).decode(FORMAT)
                if (field == "name"):
                    conn.send("Enter new name:".encode(FORMAT))
                    newName = conn.recv(SIZE).decode(FORMAT)
                    h = 0
                    customerList[n][h] = newName
                elif (field == "age"):
                    conn.send("Enter new age:".encode(FORMAT))
                    newAge = conn.recv(SIZE).decode(FORMAT)
                    h = 1
                    customerList[n][h] = newAge
                elif (field == "address"):
                    conn.send("Enter new address:".encode(FORMAT))
                    newAddress = conn.recv(SIZE).decode(FORMAT)
                    h = 2
                    customerList[n][h] = newAddress
                elif (field == "telephone"):
                    conn.send("Enter new telephone number:".encode(FORMAT))
                    newTelephone = conn.recv(SIZE).decode(FORMAT)
                    h = 3
                    customerList[n][h] = newTelephone
                conn.send("Customer information updated".encode(FORMAT))
            else:
                conn.send("Customer does not exist".encode(FORMAT))


    file.close()


    conn.close()
    print(f"[DISCONNECTED] {ADDR} disconnected.")


if __name__ == "__main__":
    main()
