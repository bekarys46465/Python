def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the value of 'n': "))
even_numbers = even_numbers_generator(n)
print("Even numbers between 0 and", n, ":", end=" ")
print(*even_numbers, sep=", ")
