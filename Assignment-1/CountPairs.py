import time
import random

random.seed(42)

n = int(input("Enter N: "))

arr = [random.randint(1, 20000) for _ in range(n)]
target = 20000

start = time.time()

count1 = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            count1 += 1

time1 = time.time() - start

start = time.time()

count2 = 0
seen = set()

for num in arr:
    complement = target - num

    if complement in seen:
        count2 += 1

    seen.add(num)

time2 = time.time() - start

print("\nTarget Sum =", target)

print("\nNaive Method:")
print("Number of pairs =", count1)
print("Time taken =", time1, "seconds")

print("\nOptimized Method:")
print("Number of pairs =", count2)
print("Time taken =", time2, "seconds")
