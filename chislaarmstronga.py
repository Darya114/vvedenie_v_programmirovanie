for a in range(1,10000+1):
    arm=0
    c=a
    i=str(a)
    while a>0:
        arm=arm+(a%10)**len(i)
        a=a//10
    if c==arm:
        print(c)
