import random
from datetime import datetime

def insertsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [random.randint(-100000, 100000) for _ in range(10000)]

start = datetime.now()
insertsort(numbers)
end = datetime.now()

print(f"Tempo de execução: {end - start}")