fibo = lambda n: n if n <= 1 else fibo(n - 1) + fibo(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibo(i), end=" ")

# output:
# Enter number of terms: 5
# 0 1 1 2 3 