names = ["A", "B", "C"]
scores = [10, 20, 30]

# enumerate
for i, n in enumerate(names):
    print(i, n)

# zip
for n, s in zip(names, scores):
    print(n, s)

# type check
x = 5
print(isinstance(x, int))