#1.
n = int(input())
sq = (x*x for x in range(1, n + 1))
for i in sq:
    print(i)

#2.
n = int(input())
sq = (x for x in range(n + 1))
for i in sq:
    if(i % 2 == 0):
        print(i)

#3.
def fun(n):
    for i in range(0, n + 1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i
n = int(input())
for x in fun(n):
    print(x)

#4.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input())
b = int(input())
for x in squares(a, b):
    print(x)

#5.
def downing(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
for x in downing(n):
    print(x)