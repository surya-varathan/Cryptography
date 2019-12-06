import timeit
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

for n in range (1,10):
    start = timeit.default_timer()
    print(multiInv(pow(10,n)-234567,pow(10,n)+1))
    elapsed=timeit.default_timer()-start
    print(elapsed)
