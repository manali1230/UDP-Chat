import socket
import threading
# import pyfiglet module 
import pyfiglet
import os

os.system("clear")
os.system("tput setaf 5")
result = pyfiglet.figlet_format("Talk", font = "doh" ) 
print(result) 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
host_port = 1234

s.bind((host_ip,host_port))

print(host_ip)

other_ip = input("Enter Your Friend's IP : ")
other_port = int(input("Enter Your Friend's port number : "))
os.system("clear")

result = pyfiglet.figlet_format("Talk", font = "doh" )
print(result)

os.system("\t\tdate")
os.system("tput setaf 6")

def Receiver():
    while True:
        os.system("tput setaf 6")
        x = s.recvfrom(1024)
        IP = x[1][0]
        data = x[0].decode()
        print("\t\t\t\t" + IP + " : " + data )
        os.system("tput setaf 0")

def Send():
    while True:
        os.system("tput setaf 5")
        message = input()
        os.system("tput setaf 5")
        s.sendto(message.encode(),(other_ip,other_port))
        if message == "bye" or message == "bye bye":
            os.system("clear")
            bye = pyfiglet.figlet_format("Bye",font="doh")
            os.system("tput setaf 4")
            print(bye)
            os.system("sleep 3")
            os.system("tput setaf 0")
            os.system("espeak-ng 'bye bye have a nice day' -s 150")
            os._exit(1)

t1 = threading.Thread(target=Receiver)
t2 = threading.Thread(target=Send)

t1.start()
t2.start()
