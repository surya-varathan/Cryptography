import timeit
def gcd(a,b):
    rem = a%b
    if a<b:
        return gcd(b,a)
    elif rem== 0:
        return b
    else:
        return gcd(b,rem)

def eulerphi(n):
    count  = 0
    for i in range(1,n):
        if(gcd(i,n)==1):
            count=count+1
    return count

def multiInv(a,n):
    if gcd(a,n)==1:
        return(pow(a,eulerphi(n)-1,n))
    else:
        return 0


for n in range (1,10):
    start = timeit.default_timer()
    print(multiInv(pow(10,n),pow(10,n)+1))
    elapsed=timeit.default_timer()-start
    print(elapsed)
