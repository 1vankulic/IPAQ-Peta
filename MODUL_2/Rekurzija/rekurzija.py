#induktivno rjesenje 
def zbroj_i(n):
    z = 0
    for i in range(1, n + 1):
        z += i 
    return z

def zbroj_r(n):
    if n == 1:
        return 1
    else:
        return zbroj_r(n - 1) + n

a = zbroj_r(5)

print(a)