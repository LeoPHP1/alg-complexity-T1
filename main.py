import time
import sys
import random
import copy
import tracemalloc
import pandas as pd

from bubbleSort import bubbleSort
from mergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort

# ==========================================
# 2. GERADOR DE CASOS DE TESTE
# ==========================================

def gerar_array(size, distribuicao):
    if distribuicao == "aleatorio":
        return [random.randint(0, size) for _ in range(size)]
    elif distribuicao == "ordenado":
        return list(range(size))
    elif distribuicao == "inverso":
        return list(range(size, 0, -1))
    elif distribuicao == "repetidos":
        universo_pequeno = [1, 2, 3, 4, 5]
        return [random.choice(universo_pequeno) for _ in range(size)]
    else:
        raise ValueError("Distribuição inválida.")

# ==========================================
# 3. MOTOR DE EXECUÇÃO (MAIN)
# ==========================================

if __name__ == "__main__":
    tamanhos_entrada = [10**3, 10**4, 10**5, 10**6] # Requisito do trabalho
    distribuicoes = ["aleatorio", "ordenado", "inverso", "repetidos"]
    
    algoritmos = [
        ("Bubble Sort", bubbleSort),
        ("Merge Sort", mergeSort),
        ("Quick Sort", quickSort),
        ("Heap Sort", heapSort)
    ]

    final_results = []

    for size in tamanhos_entrada:
        print(f"\n[{'='*40}]\nIniciando testes para Tamanho da Entrada: {size}\n[{'='*40}]")
        
        for dist in distribuicoes:
            print(f"\n  >> Gerando array ({dist})...")
            array_original = gerar_array(size, dist)
            
            for algorithm_name, funcao_sort in algoritmos:
                array_para_teste = copy.copy(array_original)
                
                # 1. Barrando o Bubble Sort para tamanhos muito grandes (qualquer distribuição)
                if algorithm_name == "Bubble Sort" and size >= 10**5:
                    print(f"    -- Ignorando {algorithm_name} (Tempo inviável para {size}).")
                    continue
                
                # 2. Barrando o Quick Sort APENAS para dados repetidos em tamanhos muito grandes
                if algorithm_name == "Quick Sort" and dist == "repetidos" and size >= 10**5:
                    print(f"    -- Ignorando {algorithm_name} para dados repetidos (Tempo/Recursão inviável para {size}).")
                    continue
                
                print(f"    Executando {algorithm_name}...")
                # ... (restante do código de medição com tracemalloc) ...
                
                # Medição de Memória
                tracemalloc.start()
                
                try:
                    metric_result = funcao_sort(array_para_teste)
                except Exception as e:
                    print(f"    Erro ao executar {algorithm_name}: {e}")
                    tracemalloc.stop()
                    continue
                
                current, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                
                # Armazenando resultados
                final_results.append({
                    "Algoritmo": algorithm_name,
                    "Tamanho": size,
                    "Distribuição": dist,
                    "Tempo (s)": round(metric_result["time"], 6),
                    "Comparações": metric_result["comparisons"],
                    "Trocas": metric_result["swaps"],
                    "Memória (Bytes)": peak_memory
                })

    # ==========================================
    # 4. EXPORTAÇÃO DOS DADOS
    # ==========================================
    print("\nExperimentos finalizados! Gerando tabelas de resultados...")
    
    df_resultados = pd.DataFrame(final_results)
    
    # Salva os resultados em um arquivo CSV (pode ser aberto no Excel/Google Sheets para gerar gráficos)
    df_resultados.to_csv("resultados_analise_ordenacao.csv", index=False)
    
    # Exibe no console uma prévia da tabela formatada
    print("\n--- PRÉVIA DOS RESULTADOS ---")
    print(df_resultados.to_string())
    print("\nTodos os dados foram salvos no arquivo 'resultados_analise_ordenacao.csv'.")
    print("Justifique a limitação do Bubble Sort no relatório, caso se aplique, conforme solicitado nas regras da atividade.")