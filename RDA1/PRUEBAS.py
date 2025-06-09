import random
import bisect
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

# 1. Lista aleatoria de 15 calificaciones
notas = random.sample(range(0, 21), 15)
notas_original = notas.copy()
print("📋 Notas originales:", notas)

# 2. Bubble Sort con visualización
def bubble_sort_visual(notas):
    notas = notas.copy()
    n = len(notas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if notas[j] > notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
            
            clear_output(wait=True)
            plt.figure(figsize=(10, 4))
            plt.bar(range(len(notas)), notas, color='skyblue')
            plt.ylim(0, 21)
            plt.title(f"Paso Bubble Sort: i={i}, j={j}")
            for k, v in enumerate(notas):
                plt.text(k, v + 0.5, str(v), ha='center')
            plt.xlabel("Índice")
            plt.ylabel("Nota")
            plt.show()
            plt.close()
            time.sleep(0.5)
    return notas

# 3. Ordenamiento con sorted() paso a paso (simulado)
def sorted_visual(notas):
    resultado = []
    sorted_notas = sorted(notas)
    for i, nota in enumerate(sorted_notas):
        resultado.append(nota)
        clear_output(wait=True)
        plt.figure(figsize=(10, 4))
        plt.bar(range(len(resultado)), resultado, color='lightgreen')
        plt.ylim(0, 21)
        plt.title(f"Inserción simulada sorted() - paso {i+1}")
        for k, v in enumerate(resultado):
            plt.text(k, v + 0.5, str(v), ha='center')
        plt.xlabel("Índice")
        plt.ylabel("Nota")
        plt.show()
        plt.close()
        time.sleep(0.5)
    return resultado

# Ejecutar visualizaciones
notas_ordenadas_bubble = bubble_sort_visual(notas_original)
notas_ordenadas_sorted = sorted_visual(notas_original)

# 4. Insertar nueva nota supletoria con bisect.insort()
nueva_nota = int(input("Ingrese una nueva nota supletoria (0 a 20): "))
bisect.insort(notas_ordenadas_sorted, nueva_nota)
print(f"Nueva nota insertada: {nueva_nota}")
print("Lista ordenada con nueva nota:", notas_ordenadas_sorted)

# 5. Buscar una nota específica
buscar_nota = int(input("🔍 Ingrese una nota a buscar: "))
pos = bisect.bisect_left(notas_ordenadas_sorted, buscar_nota)

if pos < len(notas_ordenadas_sorted) and notas_ordenadas_sorted[pos] == buscar_nota:
    print(f"Nota {buscar_nota} encontrada en la posición {pos}")
else:
    print(f"Nota {buscar_nota} no encontrada. Estaría en la posición {pos}")
