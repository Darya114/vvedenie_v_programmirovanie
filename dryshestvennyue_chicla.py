
divs=[]
for a in range(1,10000+1):
    b=0
    d=0
    for j in range(1,a):
        if a%j==0:
            b=b+j
    for j in range(1,b):
        if b%j==0:
            d=d+j
    if (a==d) and (a!=b):
        if a<b:
            divs.append((a,b))
        else:
            divs.append((b,a))
divs=sorted(set(divs))
for pairs in divs:
    print(pairs)
        

