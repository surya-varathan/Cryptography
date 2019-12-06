import math

class EC:
    def __init__(self,a,b,p):
        super().__init__()
        self.a=a
        self.b=b
        self.p=p
    def getCoeff(self):
        return(self.a,self.b)
    def multiInv(self,x):
        for i in range(1,self.p):
            if ((x*i)%self.p)==1:
                break
        return i
    def getModulus(self):
        return self.p

class Point:
    def __init__(self):
        return
    
    def __init__(self,x,y,curve):
        self.x=x
        self.y=y
        self.curve=curve

    def setVal(self,x,y,curve):
        self.x=x
        self.y=y
        self.curve=curve

    def getInverse(self):
        mod = self.curve.getModulus()
        return Point(self.x,-self.y%mod,self.curve)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
        
    def getCurve(self):
        return self.curve

    def add(self,Q):
    
        same = False
        mod = self.curve.getModulus()

        xQ = Q.getX()
        yQ = Q.getY()

        xP = self.x
        yP = self.y
        if(xP == xQ and yP==yQ):
            same = True
        if not same:
            s=((yQ-yP)*self.curve.multiInv(xQ-xP)) %mod
        else:
            co = self.curve.getCoeff()
            a = co[0]
            b = co[1]
            s = ((3*pow(xP,2)+a)*self.curve.multiInv(2*yP)) %mod
        xR = (pow(s,2) - xP -xQ) % mod
        yR = (-yP + s*(xP - xR)) % mod
        R = Point(xR,yR,self.curve)

        return R
    
    def multiply(self,n):
        co = self.curve.getCoeff()
        mod = self.curve.getModulus()

        xQ = self.x
        yQ = self.y
        
        xP = self.x
        yP = self.y
        a = co[0]
        b = co[1]
        s = ((3*pow(xP,2)+a)*self.curve.multiInv(2*yP))%mod

        xR = (pow(s,2) - xP -xQ) % mod
        yR = (-yP + s*(xP - xR)) % mod
        
        R = Point(xR,yR,self.curve)
        Q = Point(xQ,yQ,self.curve)

        for i in range(0,n-2):
            R = R.add(Q)
        
        return R
    
