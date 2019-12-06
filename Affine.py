def euclideanGCD(a,b):
        if(b==0):
            return a
        else:
            return(euclideanGCD(b,a%b))


class AffineCipher:
    
    def __init__(self,m):
        self.m = m
        self.alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        self.num ='abcdefghijklmnopqrstuvwxyz'
 
    def multiInv(self,a):
        for i in range(1,self.m-1):
            if ((i*a)%self.m == 1):
                break
        return i

    def addInv(self,a):
        if(a<0):
            return a%self.m
        else:
            return self.m - a%self.m

    def isKeyValid(self,a):
        if(euclideanGCD(self.m,a)==1):
            return True
        else:
            return False

    def encrypt(self,msg):
        key=input("Enter a,b pair:")
        list=key.split(',')
        key = []
        for i in list:
            key.append(int(i))
        #key=tuple(key)
        while(not self.isKeyValid(key[0])):
            key[0]=int(input("Re-enter a valid 'a'"))
        cipher=""
        for i in msg:
            x = self.alpha[i]
            c = ( key[0]*x+key[1] ) % self.m
            y=self.num[c]
            cipher=cipher+y
        return cipher
    def decrypt(self,cipher):
        key=input("Enter a,b pair:")
        list=key.split(',')
        key = []
        for i in list:
            key.append(int(i))
        #key=tuple(key)
        while(not self.isKeyValid(key[0])):
            key[0]=int(input("Re-enter a valid 'a'"))
        msg=""
        for i in cipher:
            x = self.alpha[i]
            c = self.multiInv(key[0])*(x - key[1]) % self.m
            y=self.num[c]
            msg=msg+y
        return msg




    
Z= AffineCipher(26)
message="helloworld"
print(message)
cipher=Z.encrypt(message)
print(cipher)
print(Z.decrypt(cipher))

