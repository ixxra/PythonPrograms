'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

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
