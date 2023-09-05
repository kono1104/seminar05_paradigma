a, b = int(input('a=')), int(input('b='))
def p(a, b):
    lst = []
    for n in range(a, b + 1):
        test = True
        k = n - 1
        while k > 1:
            if n % k == 0:
                test = False
                break
            k -= 1
        if test:
            lst.append(n)
            print(n)
    return lst
print (p(a,b))

    
