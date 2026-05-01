numbers = list(map(int, input().split()))
odd_numbers = list(filter(lambda x: x > 0 and x % 2 == 0, numbers))
print(odd_numbers)