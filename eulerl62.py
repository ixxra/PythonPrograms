from time import time
aa=time()
C=[i**3 for i in range(22,100000)]
cadenas=[]

for i in xrange(len(C)):
    f=[str(d) for d in str(C[i])]
    f.sort()
    cadenas.append(f)

for m in xrange(len(strs)):
    gg=cadenas.count(cadenas[m])
    if gg==5:
        break

print C[m],cadenas[m],m
print time()-aa
