def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
for number in numbers_down_to_zero(n):
    print(number)
