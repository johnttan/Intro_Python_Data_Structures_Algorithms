import timeit
def recfibo(num, one, two):
    if num <= 0:
        return
    elif one == 0:
        # print(one)
        # print(two)
        recfibo(num-2, two, one+two)
    else:
        # print(two)
        recfibo(num-1, two, one+two)

def iterativefibo(num):
    one, two = 0, 1
    while num >= 0:
        fibo = one + two
        one, two = two, fibo
        num -= 1

print(timeit.timeit('recfibo(10, 0, 1)', "from __main__ import recfibo"), 'recursive')
print(timeit.timeit('iterativefibo(10)', "from __main__ import iterativefibo"), 'iterative')
# Iterative far more efficient because of function overhead. Iterative approach is O(n). Function call stack?