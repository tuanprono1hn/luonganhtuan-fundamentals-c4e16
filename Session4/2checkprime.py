n = int(input("Enter a number: "))
isprime = True
# for i in range(2, n):
#     if n % i == 0:
#         isprime = False
#         break

i = 2

while i <= (n ** 0.5):
    if n % i == 0:
        isprime = False
        break
    i += 1

if isprime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
