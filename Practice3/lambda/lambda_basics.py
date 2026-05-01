p, q, r = map(int, input().split())
x = lambda a, b, c : ((a + b + c) / 2 *((a + b + c) / 2 - a)*((a + b + c) / 2 - b)*((a + b + c) / 2 - c)) ** (1/2)
print(x(p, q, r))