divs=[]
for a in range(1,10000+1):
    b=0
    d=0
    e=0
    for j in range(1,a):
        if a%j==0:
            b=b+j
            e=b-1
    for j in range(1,e):
        if e%j==0:
            d=d+j
    if (a==d-1) and (a!=b):
        if a<e:
            divs.append((a,e))
        else:
            divs.append((e,a))
divs=sorted(set(divs))
for pairs in divs:
    print(pairs)