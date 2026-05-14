import time
import sys
def heap_sort(arr):
    comparisons = [0]
    swaps = [0]

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            comparisons[0] += 1
            if arr[l] > arr[largest]:
                largest = l

        if r < n:
            comparisons[0] += 1
            if arr[r] > arr[largest]:
                largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps[0] += 1
            heapify(n, largest)

    start_time = time.perf_counter()
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
        
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swaps[0] += 1
        heapify(i, 0)
        
    end_time = time.perf_counter()
    
    return {"time": end_time - start_time, "comparisons": comparisons[0], "swaps": swaps[0]}