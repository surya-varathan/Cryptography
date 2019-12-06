from ECC import *
import math
import random
import socket
import threading
import pickle
MAX_CHUNK = 8*1024

sec_rand = random.SystemRandom()         

class ECCEG:
    def __init__(self):
        self.host=socket.gethostbyname(socket.gethostname())
        print(self.host)
        self.port = 12345
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
        self.server.bind((self.host,self.port))
        self.curve = EC(2,3,67)

    def keyGenPhase(self):
        e1 = Point(2,22,self.curve)
        d = random.randint(2,self.curve.getModulus())
        e2 = e1.multiply(d)
        return [self.curve,e1,e2,d]

    def decryptor(self,c1,c2,d):
        temp = c1.multiply(d)
        tempInv = temp.getInverse()
        p = c2.add(tempInv)
        return p

    def client_thread(self,conn,addr):
        keys=self.keyGenPhase()
        pvtKey = keys.pop()
        pubKey = keys
        conn.send(pickle.dumps(pubKey))
        cipher=pickle.loads(conn.recv(MAX_CHUNK))
        message=self.decryptor(cipher[0],cipher[1],pvtKey)
        print(message.getX(),message.getY(),sep=',')


    def listen(self):
        self.server.listen(5)
        while True:
            
            conn,addr = self.server.accept()
            print("Connected with ",addr)
            try:
                t1=threading.Thread(target=self.client_thread,args=(conn,addr))
                t1.start()
                print("Thread started")

            except:
               print("Thread did not start")
                
        
        self.sock.close()


e = ECCEG()
e.listen()
