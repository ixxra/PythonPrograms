'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''


import time
def primesbeforen(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i):
                S[m*i]=False
    #print S
    print sum(P)



r=2000000
comienzo=time.time()
print primesbeforen(r)
final=time.time()
print "Tiempo tardado :D :" , final - comienzo
