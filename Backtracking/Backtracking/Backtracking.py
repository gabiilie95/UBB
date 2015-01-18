#   3. Generati toate permutarile de dimensiune n (1..n), cu proprietatea ca pentru orice i 2<=i<=n
#   exista un j, 1<=j<=i astfel incat |v(i)-v(j)|=1.
#
def valid(v):
    nr = len(v) - 1
    for i in range(1, len(v)):
        ok = 0
        for j in range (1, i+1):
            if j == i+1 or j == i-1:
                ok = 1
        if ok == 0: 
            return False
    return True
    
def permut(v, n):
    if len(v) == n:
        print (v)
    if len(v) > n:
        return
    v.append(0)
    for i in range (0, n):
        v[-1] = i
        if valid(v):
            permut(v[:], n)

permut([], 4)

