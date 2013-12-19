def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i):
                S[m*i]=False
    return P
K=primes(10**6)
for i in range(len(K)-1):
    N=str(K[i])
    