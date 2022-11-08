s=0
r= 1.4
n=0
while n < 2.8*10**7:
    s += r*(n - r)/(n*n*n + 1)
    n += 1
print(s)
