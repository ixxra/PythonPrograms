for i in range(10,19):
    a=[i for i in str(i)]
    for j in range(10,19):
        b=[u for u in str(j)]    
        x=a[0]
        y=a[1]
        w=b[0]
        z=b[1]
        p= x==w 
        q= x==z 
        r= y==w 
        s= y==z
        if y=='0' or x=='0':
            #print i,j, 'tururu'
        else:
            if (p or q or r or s) ==True:
                if p==True:
                    if float(int(y))/int(z)==float(i)/j:
                        print i,j
                if q==True:
                    if float(int(y))/int(w)==float(i)/j:
                        print i,j
                if r==True:
                    if float(int(x))/int(z)==float(i)/j:
                        print i,j
                if s==True:
                    if float(int(x))/int(w)==float(i)/j:
                        print i,j
    
