from socket import *
import time

addr = ("127.0.0.1", 12000) #Connects localhost to port 12000

for ping in range(1, 11): #Sends the ping 10 times (1 <= ping < 11)
    clientSocket = socket(AF_INET, SOCK_DGRAM) #Sets up a UDP Socket
    clientSocket.settimeout(1) #Waits 1 second before request times out

    message = raw_input('PING ') #Sends message to server

    startTime = time.time() #Starts RTT timer
    clientSocket.sendto(message, addr) #Sends message to addr

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #Receives message
        endTime = time.time() #If message received, ends RTT timer
        rtt = endTime - startTime #Calculates RTT
        print '{0} {1} {2}'.format('Ping', ping, rtt) #Displays Ping, ping# and RTT

    except timeout:
        print 'Request timed out' #Prints request timed out

clientSocket.close() #Closes clientSocket
