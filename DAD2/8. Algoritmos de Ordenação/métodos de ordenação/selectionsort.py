import random
from datetime import datetime

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [random.randint(-100000, 100000) for _ in range(10000)]

start = datetime.now()
selectionsort(numbers)
end = datetime.now()

print(f"Tempo de execução: {end - start}")