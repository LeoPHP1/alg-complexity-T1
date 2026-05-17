import time

#Função perf_counter() da biblioteca time marca o tempo de inicio 
# e fim da execução do algoritmo de forma precisa

def mergeSort(arr):
    comparisons = [0] 
    movements = [0]   

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                movements[0] += 1
                i += 1
            else:
                result.append(right[j])
                movements[0] += 1
                j += 1
        
        while i < len(left):
            result.append(left[i])
            movements[0] += 1
            i += 1
        while j < len(right):
            result.append(right[j])
            movements[0] += 1
            j += 1
        return result

    def sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])
        return merge(left, right)

    start_time = time.perf_counter()
    sorted_arr = sort(arr)
    # Copiando de volta para o array original (in-place simulado para manter consistência de uso)
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]
        movements[0] += 1
    end_time = time.perf_counter()
    
    return {"time": end_time - start_time, "comparisons": comparisons[0], "swaps": movements[0]}