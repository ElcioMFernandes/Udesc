import random
from datetime import datetime

def bucketsort(arr, nbuckets=10):
    if not arr:
        return arr

    if len(arr) == 1:
        return arr

    minimal = arr[0]
    maximal = arr[0]

    for num in arr:
        if num < minimal:
            minimal = num
        
        if num > maximal:
            maximal = num

    if minimal == maximal:
        return arr

    if nbuckets <= 0:
        raise ValueError("Number of buckets must be greater than 0")

    buckets = [[] for _ in range(nbuckets)]


    for num in arr:
        if nbuckets == 1:
            buckets[0].append(num)
        else:
            index = int((num - minimal) / (maximal - minimal) * (nbuckets - 1))
            buckets[index].append(num)

    sortedarr = []
    for i in range(nbuckets):
        if buckets[i]:
            sortedarr.extend(bucketsort(buckets[i], nbuckets))

    return sortedarr

if __name__ == "__main__":
    numbers = [random.randint(-100000, 100000) for _ in range(10000)]
    
    start = datetime.now()
    print(bucketsort(numbers, int(len(numbers)/2)))
    end = datetime.now()

    print(f"Tempo de execução: {end - start}")