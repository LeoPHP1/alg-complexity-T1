import time
import sys

#Função perf_counter() da biblioteca time marca o tempo de inicio 
# e fim da execução do algoritmo de forma precisa

def quickSort(arr):
    comparisons = [0]
    swaps = [0]

    def partition(low, high):
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
        # Aumentando limite de recursão para arrays ordenados/inversos
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr) + 100))
    start_time = time.perf_counter()
    sort(0, len(arr) - 1)
    end_time = time.perf_counter()
    
    return {"time": end_time - start_time, "comparisons": comparisons[0], "swaps": swaps[0]}