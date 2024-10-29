def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivô = lista[len(lista) // 2]
        menor = [x for x in lista if x < pivô]
        igual = [x for x in lista if x == pivô]
        maior = [x for x in lista if x > pivô]
        return quick_sort(menor) + igual + quick_sort(maior)

# Exemplo de uso:
numeros = [5, 2, 9, 1, 7, 3]
print(quick_sort(numeros))  # Saída: [1, 2, 3, 5, 7, 9]