
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact = dict()
for n in range(1, 10):
    fact[n] = factorial(n)
fact[0] = 1

def digits(n):
    tmp = n
    result = []
    while tmp > 0:
        result.append(tmp % 10)
        tmp /= 10
    return result

def test(n):
    d = digits(n)
    s = 0
    for i in d:
        s += fact[i]
    return s == n

s = 0
for n in range(3, 2540161):
    if test(n):
        print n
        s += n
print s
