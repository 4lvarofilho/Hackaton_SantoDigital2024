def pairs_with_smallest_difference(arr):
    # Ordena o array para tornar mais fácil encontrar pares com a menor diferença
    arr.sort()
    smallest_difference = float('inf')
    pairs = []
    # Percorre o array para encontrar a menor diferença
    for i in range(len(arr) - 1):
        difference = arr[i + 1] - arr[i]
        if difference < smallest_difference:
            smallest_difference = difference
            pairs = [(arr[i], arr[i + 1])]
        elif difference == smallest_difference:
            pairs.append((arr[i], arr[i + 1]))
    return pairs
# Exemplo de utilização
array = [5, 7, 4, 3, 2]
result = pairs_with_smallest_difference(array)
print(result)  # Output: [(2, 3), (3, 4), (4, 5)]