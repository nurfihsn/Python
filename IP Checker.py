from ipaddress import ip_address
import socket

host = input ("Masukkan nama domain: ")
ip_address = socket.gethostbyname (host)

print(f"Nama domain: {host}")
print (f"IP address: {ip_address}")