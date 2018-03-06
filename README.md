# UDP Pinger

In this repository is a UDP pinger and a UDP client that simulates a UDP datagram object request and retrieval between a server and client. The server is also programmed to drop a certain amount of requests to simulate a drop in request or failure in communication between the server and client.

## Instructions for use

  1) Download the repository
  2) Run the `UDPPingerServer.py` using Python 2.7
  3) Now run `UDPPingerClient.py` using Python 2.7 and type in 10 different requests one by one to see it's RTT and whether or not the request was received or lost.
