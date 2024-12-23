def  bubblesort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [i for i in lista[1:] if i <= pivot]
        greater = [i for i in lista[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    