from ECC import *
import socket
import pickle
import random

MAX_CHUNK =8*1024

class Client:
	def __init__(self,addr):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.client.connect((addr[0],int(addr[1])))
		self.pubKey = pickle.loads(self.client.recv(MAX_CHUNK))
	def encryption(self,P,e1,e2):
		curve = P.getCurve()
		r = random.randint(2,curve.getModulus())
		c1 = e1.multiply(r)
		temp = e2.multiply(r)
		c2 = P.add(temp)
		print("Encrypted points:\nC1: ",c1.getX(),",",c1.getY(),"\n","C2: ",c2.getX(),",",c2.getY())
		return [c1,c2]
	def foo(self):
		x = int(input("Enter X\n"))
		y = int(input("Enter Y\n"))
		curve = self.pubKey[0]
		P = Point(x,y,curve)
		cipher = self.encryption(P,self.pubKey[1],self.pubKey[2])
		self.client.send(pickle.dumps(cipher))


addr = input('Enter the IP and Port no\n')
addr =  addr.split(sep=" ")

c = Client(addr)
c.foo()
 
