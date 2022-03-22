n,m = map(int,input().split())

def gcd(n,m):
    if n%m == 0:
        return m
    else:
        return gcd(m, n%m)
print(m - gcd(n,m))