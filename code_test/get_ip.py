import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

a_dictionary = {"a" : 1, "b" : 2}

file = open("sample.txt", "w")
str_dictionary = repr(hostname)
str_localip = repr(local_ip)
file.write("hostname, local_ip = " + str_dictionary + str_localip + "\n")


#print(local_ip, hostname)