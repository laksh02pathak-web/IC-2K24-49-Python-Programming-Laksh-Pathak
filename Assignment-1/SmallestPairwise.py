
import time
import random

random.seed(42)

n = int(input("Enter N: "))
k = int(input("Enter K: "))

arr = [random.randint(1, 100000) for _ in range(n)]

if n < 2 or k < 1 or k > n * (n - 1) // 2:
    print("Invalid value of K")
else:
    start = time.time()

    sums = []

    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])

    sums.sort()
    result1 = sums[k - 1]

    time1 = time.time() - start

    start = time.time()

    arr.sort()

    def count_pairs(value):
        left = 0
        right = n - 1
        count = 0

        while left < right:
            if arr[left] + arr[right] <= value:
                count += right - left
                left += 1
            else:
                right -= 1

        return count

    low = arr[0] + arr[1]
    high = arr[n - 2] + arr[n - 1]

    while low < high:
        mid = (low + high) // 2

        if count_pairs(mid) >= k:
            high = mid
        else:
            low = mid + 1

    result2 = low

    time2 = time.time() - start

    print("\nK-th Smallest Pairwise Sum:", k)

    print("\nNaive Method:")
    print("Result =", result1)
    print("Time taken =", time1, "seconds")

    print("\nOptimized Method:")
    print("Result =", result2)
    print("Time taken =", time2, "seconds")
