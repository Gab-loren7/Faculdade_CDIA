'''
Vamos testar a aceleração que um cache em memória pode oferecer. Para isso, imagine que a nossa
função buscar exige 50 ms para executar, tal como mostrado abaixo:

## Função buscar que retorna chave + float aleatório

def buscar (chave):
    time.sleep(0.050)   #50ms
    return chave + str(random.random())

Implemente uma função chamada buscar_cache(), capaz de receber a chave e chamar a função
buscar apenas se necessário.

Compare o tempo de execução de 1.000 chamadas em “buscar” com “buscar_cache”. Qual o ganho
% usando o cache?

Há ganho se as chaves são todas diferentes em buscar_cache?

Use time.time() para medir o tempo. Essa função retorna o tempo em segundos (+ frações). Basta
executar antes e depois e pegar a diferença.

'''
import time
import random

# Dicionário global que funcionará como a nossa memória (Cache)
cache_memoria = {}

def buscar(chave):
    """Simula uma busca lenta (ex: consulta a um banco de dados)"""
    time.sleep(0.050)  # Pausa de 50ms
    return chave + ":" + str(random.random())

def buscar_cache(chave):
    """
    Verifica se a chave já foi processada antes.
    Se sim, entrega o resultado imediato. Se não, chama 'buscar'.
    """
    if chave in cache_memoria:
        # Se a chave já está no dicionário, apenas retornamos o valor
        return cache_memoria[chave]
    else:
        # Se não está, calculamos, guardamos no cache e retornamos
        resultado = buscar(chave)
        cache_memoria[chave] = resultado
        return resultado

# --- TESTE DE PERFORMANCE ---

# Vamos testar com uma lista de chaves onde muitas se repetem
# para que o cache tenha utilidade.
chaves_para_testar = ["user_1", "user_2", "user_3"] * 333 # Gera 999 chamadas repetidas

print("Iniciando testes para 1.000 chamadas...")

# 1. Medindo tempo SEM cache
inicio_sem = time.time()
for c in chaves_para_testar:
    buscar(c)
fim_sem = time.time()
tempo_total_sem = fim_sem - inicio_sem

# 2. Medindo tempo COM cache
inicio_com = time.time()
for c in chaves_para_testar:
    buscar_cache(c)
fim_com = time.time()
tempo_total_com = fim_com - inicio_com

# --- RESULTADOS ---

ganho_percentual = ((tempo_total_sem - tempo_total_com) / tempo_total_sem) * 100

print(f"\nTempo SEM cache: {tempo_total_sem:.2f} segundos")
print(f"Tempo COM cache: {tempo_total_com:.2f} segundos")
print(f"Ganho de performance: {ganho_percentual:.2f}%")