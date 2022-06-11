print({1,2}.issubset({3,2,1}))
t = set()
# while not t.issubset({1,2,3,4,5,6,7,8}):
def s1(a,b,c,d):
    res = {a,b,c,d}
    res.add(a+b)
    res.add(b+c)
    res.add(c+d)
    res.add(a + b+c)
    res.add(b+c+d)
    res.add(b + c + d+a)
    return res
for a in range(-10,50):
    for b in range(-10,50):
        for c in range(-10,50):
            for d in range(-10,50):
                if {1,2,3,4,5,6,7,8}.issubset(s1(a,b,c,d)):
                    print(a,b,c,d)
                    break