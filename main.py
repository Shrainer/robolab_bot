def fibn(n):
    if n in (2,3):
        return 1
    if n ==1:
        return 0
    return fibn(n-1) + fibn(n-2)

print(fibn(4))
