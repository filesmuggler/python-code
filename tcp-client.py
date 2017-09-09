import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

raw_data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
data = ''

for symbol in raw_data:
    symbol = format(ord(symbol),"x")    
    data = data + symbol




# send some data
client.send(data)

# recieve some data
response = client.recv(4096)

print("It's response from server:\n")
print(response)

file = open('result-google.txt','w')
response = str(response)
file.write(response)
file.close()


