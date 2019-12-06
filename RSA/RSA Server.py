import math
import random
import socket
import threading
import pickle
MAX_CHUNK = 8*1024

sec_rand = random.SystemRandom()         

'''
    Basic math functions for ASK
'''

def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b == 0:
        return b
    else:
        return gcd(b,a%b)

def eulerphi(n):
    count  = 0
    for i in range(1,n):
        if(gcd(i,n)==1):
            count=count+1
    return count

def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def multiInv(a,n):
       temp = xgcd(n,a)
       inv = temp[2]
       inv = (n + inv)%n
       if(temp[0]!=1):
           inv = -1
       return inv

def groupGen(n):
    group = []
    e=1
    while (e<n):
        if(math.gcd(e,n)==1):
            group.append(e)
        e=e+1
    return group

def miillerTest(d, n): 

    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)
  
    if (x == 1 or x == n - 1): 
        return True; 

    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True;  
    return False; 
  
def isPrime(n): 
       
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
  
    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 
 
    for i in range(4): 
        if (miillerTest(d, n) == False): 
            return False; 
  
    return True; 

def prime_gen(x,y):
       prime=False
       while(prime is False):
              p = random.randint(x,y)
              prime = isPrime(p)
       return p

class RSA:
    def __init__(self):
        self.host=socket.gethostbyname(socket.gethostname())
        print(self.host)
        self.port = 12345
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
        self.server.bind((self.host,self.port))

    def keyGenPhase(self):
        p=prime_gen(pow(10,2),pow(10,3))
        print(p)
        q=prime_gen(pow(10,2),pow(10,3))
        print(q)
        n = p*q
        print(n)
        phi = (p-1)*(q-1)
        print(phi)
        flag = True
        while flag:
            e = random.randint(2,phi)
            if(gcd(e,phi)==1):
                break
        print(e)
        d = multiInv(e,phi)
        print(d)
        return([e,n,d])

    def decryptor(self,cipher,d,n):
        msg = [chr(pow(ord(char),d,n)) for char in cipher]
        decrypted = ""
        for i in msg:
            decrypted += i
        return decrypted

    def client_thread(self,conn,addr):
        keys=self.keyGenPhase()
        print(keys)
        pvtKey = keys.pop()
        pubKey = keys
        
        conn.send(pickle.dumps(pubKey))
        cipher=pickle.loads(conn.recv(MAX_CHUNK))
        message=self.decryptor(cipher,pvtKey,pubKey[1])
        print(message)


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


r = RSA()
r.listen()
