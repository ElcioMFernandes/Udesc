import random
from datetime import datetime

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)

numbers = [random.randint(-100000, 100000) for _ in range(10000)]

start = datetime.now()
quicksort(numbers)
end = datetime.now()

print(f"Tempo de execução: {end - start}")