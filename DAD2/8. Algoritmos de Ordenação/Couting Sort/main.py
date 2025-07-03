def coutingsort(arr):
    if not arr:
        return []

    maximal = max(arr)
    minimal = min(arr)

    if len(arr) == 1 or maximal == minimal:
        return arr

    counter = [0] * maximal
    
    print(arr)
    for i, j in enumerate(set(arr)):
        count = 0

        for k in arr:
            if k == j:
                count += 1
        
        counter[i] = count
    print(counter)

    for i, j in enumerate(counter):
        if i != 0:
            counter[i] += counter[i - 1]
    print(counter)

if __name__ == "__main__":
    coutingsort([3, 2, 1, 3, 2, 2, 1])
    #print(coutingsort([1, 2, 3, 3]))