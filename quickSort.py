import time
import sys
import random

def quickSort(arr):
    comparisons = [0]
    swaps = [0]

    def partition(low, high):
        # CORREÇÃO PARA O PIOR CASO: Escolha de Pivô Aleatório
        # Escolhemos um índice aleatório no pedaço atual do array
        pivot_index = random.randint(low, high)
        
        # Trocamos o elemento aleatório com o último elemento
        # Assim, o restante da lógica original do Quick Sort funciona perfeitamente
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps[0] += 1
        
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    # Mantemos o aumento de recursão por segurança, 
    # embora com o pivô aleatório ele dificilmente será atingido
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr) + 100))
    
    start_time = time.perf_counter()
    sort(0, len(arr) - 1)
    end_time = time.perf_counter()
    
    return {"time": end_time - start_time, "comparisons": comparisons[0], "swaps": swaps[0]}