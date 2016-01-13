def pi(n, m):
    if n <= 1:
        return 1
    if m>n:
        return pi(n,n)
    summ = 0
    for k in range(1, m + 1):
        summ += pi(n-k,k)
    return summ

def p(n):
    return pi(n,n)

print(p(100) -1)
