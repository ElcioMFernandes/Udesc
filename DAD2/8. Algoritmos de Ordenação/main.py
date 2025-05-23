from datetime import datetime

def quicksort(arr):
    if len(arr) <= 1: # Se o tamanho do array for menor ou igual a 1, já está ordenado
        return arr
    
    else:
        pivot = arr[0] # Escolhe o primeiro elemento como pivô

        left = [x for x in arr[1:] if x < pivot] # Para cada elemento no array, se for menor que o pivô, adiciona à lista da esquerda

        right = [x for x in arr[1:] if x >= pivot] # Para cada elemento no array, se for maior ou igual ao pivô, adiciona à lista da direita

        return quicksort(left) + [pivot] + quicksort(right) # Retorna o resultado dos arrays menores + o pivô + o resultado dos arrays maiores

start = datetime.now() # Inicia o cronômetro
print(quicksort([1, 7, 4, 1, 10, 9, -2]))
end = datetime.now() # Para o cronômetro

print(f"Tempo de execução: {end - start}")