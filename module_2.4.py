numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for x in numbers:
    if x == 1:
        continue
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
    if is_prime == True:
        primes.append(x)
    else:
        not_primes.append(x)
print(primes)
print(not_primes)