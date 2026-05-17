import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

try:
    df = pd.read_csv("resultados_analise_ordenacao.csv")
except FileNotFoundError:
    print("Erro: Arquivo 'resultados_analise_ordenacao.csv' não encontrado.")
    exit()

# Cria uma pasta para salvar os gráficos
os.makedirs("report_graphs", exist_ok=True)

# 1. Tempo de execução em função do tamanho da entrada (Por Distribuição)
distribuicoes = df['Distribuição'].unique()

for dist in distribuicoes:
    plt.figure(figsize=(10, 6))
    df_dist = df[df['Distribuição'] == dist]
    
    # Criando gráfico de linhas
    ax = sns.lineplot(data=df_dist, x='Tamanho', y='Tempo (s)', hue='Algoritmo', style='Algoritmo', markers=True, dashes=False)
    
    # Usando escala logarítmica (essencial já que a entrada vai de 10^3 a 10^6)
    plt.xscale('log')
    plt.yscale('log') # Tempo também cresce muito rápido
    
    plt.title(f'Tempo de Execução vs Tamanho da Entrada\nDistribuição: {dist.capitalize()}', fontsize=14)
    plt.xlabel('Tamanho da Entrada (Escala Log)', fontsize=12)
    plt.ylabel('Tempo de Execução (Segundos - Escala Log)', fontsize=12)
    plt.legend(title='Algoritmo')
    
    plt.tight_layout()
    plt.savefig(f"report_graphs/1_tempo_vs_tamanho_{dist}.png", dpi=300)
    plt.close()

# 2. Consumo de memória em função do tamanho da entrada (Por Distribuição)
for dist in distribuicoes:
    plt.figure(figsize=(10, 6))
    df_dist = df[df['Distribuição'] == dist]
    
    sns.lineplot(data=df_dist, x='Tamanho', y='Memória (Bytes)', hue='Algoritmo', style='Algoritmo', markers=True, dashes=False)
    
    plt.xscale('log')
    # A memória pode não precisar de escala log dependendo do algoritmo, mas ajuda a ver o todo
    plt.yscale('log') 
    
    plt.title(f'Pico de Consumo de Memória vs Tamanho da Entrada\nDistribuição: {dist.capitalize()}', fontsize=14)
    plt.xlabel('Tamanho da Entrada (Escala Log)', fontsize=12)
    plt.ylabel('Pico de Memória (Bytes - Escala Log)', fontsize=12)
    plt.legend(title='Algoritmo')
    
    plt.tight_layout()
    plt.savefig(f"report_graphs/2_memoria_vs_tamanho_{dist}.png", dpi=300)
    plt.close()

# 3. Comparação entre algoritmos para cada tipo de distribuição 
#    (Fixando um tamanho onde todos rodam, ex: 10^4)
# =====================================================================
# Escolhemos 10^4 porque todos os algoritmos (inclusive o Bubble) rodam neste tamanho.
tamanho_fixo = 10**4
df_fixo = df[df['Tamanho'] == tamanho_fixo]

plt.figure(figsize=(12, 6))
sns.barplot(data=df_fixo, x='Distribuição', y='Tempo (s)', hue='Algoritmo')

plt.title(f'Comparação de Algoritmos por Distribuição (Tamanho Fixo: {tamanho_fixo})', fontsize=14)
plt.ylabel('Tempo de Execução (Segundos)', fontsize=12)
plt.xlabel('Distribuição dos Dados', fontsize=12)

# Adiciona escala log no Y para melhor visualização (Bubble Sort distorce o gráfico linearmente)
plt.yscale('log')

plt.tight_layout()
plt.savefig(f"report_graphs/3_comparacao_algoritmos_tamanho_{tamanho_fixo}.png", dpi=300)
plt.close()

# BÔNUS: Comparação para tamanho 10^5 (Aqui o Bubble Sort sumirá e o Quick Sort Repetido também)
tamanho_fixo_grande = 10**5
df_fixo_grande = df[df['Tamanho'] == tamanho_fixo_grande]

if not df_fixo_grande.empty:
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_fixo_grande, x='Distribuição', y='Tempo (s)', hue='Algoritmo')
    plt.title(f'Comparação de Algoritmos (Tamanho: {tamanho_fixo_grande})\n(Observe a ausência dos algoritmos barrados)', fontsize=14)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig(f"report_graphs/3_comparacao_algoritmos_tamanho_{tamanho_fixo_grande}.png", dpi=300)
    plt.close()

# =====================================================================
# 4. Comparação entre diferentes distribuições para um mesmo algoritmo
# =====================================================================
algoritmos = df['Algoritmo'].unique()

for algo in algoritmos:
    plt.figure(figsize=(10, 6))
    df_algo = df[df['Algoritmo'] == algo]
    
    sns.lineplot(data=df_algo, x='Tamanho', y='Tempo (s)', hue='Distribuição', style='Distribuição', markers=True, dashes=False)
    
    plt.xscale('log')
    plt.yscale('log')
    
    plt.title(f'Impacto da Distribuição dos Dados no Desempenho\nAlgoritmo: {algo}', fontsize=14)
    plt.xlabel('Tamanho da Entrada (Escala Log)', fontsize=12)
    plt.ylabel('Tempo de Execução (Segundos - Escala Log)', fontsize=12)
    plt.legend(title='Distribuição')
    
    plt.tight_layout()
    plt.savefig(f"report_graphs/4_impacto_distribuicao_{algo.replace(' ', '_')}.png", dpi=300)
    plt.close()

print("Todos os gráficos foram gerados e salvos na pasta 'report_graphs/'.")