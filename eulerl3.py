import time
def factor(t):
    a=[]
    while t%2==0:
        t=t/2
        a=a+[2]
    for i in range(3,int(t**.5)+1,2):
        if t<=1:
            break
        else:
            while t%i==0:
                a=a+[i]
                t=t/i
    a=a+[t]

    return a
k= time.time()
#print factor(600851475143 )
#for i in range(2000,2050):
#    print i, factor(i)
print factor(2014)

b= time. time()
