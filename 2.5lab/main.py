def fact(n):
    if n == 0: # 0! = 1
        return 1
    return fact(n - 1) * n # n! = (n - 1)! * n
