import socket
import pickle
MAX_CHUNK =8*1024

class Client:
	def __init__(self,addr):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.client.connect((addr[0],int(addr[1])))
		self.pubKey = pickle.loads(self.client.recv(MAX_CHUNK))
	def encryption(self,message,e,n):
		cipher = [pow(ord(char),e,n) for char in message]
		encrypted=""
		for char in cipher:
			temp=chr(char)
			encrypted+=temp
		return encrypted
	def foo(self):
		message = input("Enter your message\n")
		cipher = self.encryption(message,self.pubKey[0],self.pubKey[1])
		self.client.send(pickle.dumps(cipher))
		print(cipher)


addr = input('Enter the IP and Port no\n')
addr =  addr.split(sep=" ")

c = Client(addr)
c.foo()
 
