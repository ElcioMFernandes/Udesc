import random
from datetime import datetime

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [random.randint(-100000, 100000) for _ in range(10000)]

start = datetime.now()
bubblesort(numbers)
end = datetime.now()

print(f"Tempo de execução: {end - start}")