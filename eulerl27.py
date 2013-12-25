import time
sss=time.time()
def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i+1):
                if m*i<len(S):
                    S[m*i]=False
    return P
RES=primes(50000)
MRES=[res*-1 for res in RES]
K=primes(1000)
K.remove(2)
tmax=40
solution=(0,0,0)
for z in range(len(K)):
    b=K[z]
    for j in range(1,1000,2):
        print z,j
        a=j
        s1=(RES.count(a+b+1)!=0)
        s2=(RES.count(a-b+1) !=0 or MRES.count(a-b+1) !=0)
        s3=(RES.count(b-a+1) !=0 or MRES.count(a-b+1) !=0)
        s4=MRES.count(-a-b+1)
        if s1==True:
            f= lambda n: n**2 + n*a + b
            e=0
            t=0
            while RES.count(f(t)) >0 or MRES.count(f(t))>0:
                t+=1
            if t>tmax:
                tmax=t
                solution=(t,a,b)
        if s2==True:
            f= lambda n: n**2 +a*n -b
            e=0
            t=0
            while RES.count(f(t)) >0 or MRES.count(f(t))>0:
                t+=1
            if t>tmax:
                tmax=t
                solution=(t,a,-b)
        if s3 ==True:
            f= lambda n: n**2 - a*n + b
            e=0
            t=0
            while RES.count(f(t)) >0 or MRES.count(f(t))>0:
                t+=1
            if t>tmax:
                tmax=t
                solution=(t,-a,b)
        if s4==True:
            f= lambda n: n**2 -a*n -b
            e=0
            t=0
            while RES.count(f(t)) >0 or MRES.count(f(t))>0:
                t+=1
            if t>tmax:
                tmax=t
                solution=(t, -a, -b)
print solution
print time.time()-sss