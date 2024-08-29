def pairs_with_smallest_difference(arr, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    # Ordena o array para tornar mais fácil encontrar pares com a menor diferença
    arr.sort()
    smallest_difference = float('inf')
    pairs = []

    # Percorre o array para encontrar a menor diferença
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if not allow_duplicates and arr[i] == arr[j]:
                continue
            difference = abs(arr[i] - arr[j])
            if difference < smallest_difference:
                smallest_difference = difference
                pairs = [(arr[i], arr[j])]
            elif difference == smallest_difference:
                pairs.append((arr[i], arr[j]))
    # Remove pares duplicados se unique_pairs for True
    if unique_pairs:
        pairs = list(set(tuple(sorted(pair)) for pair in pairs))
    # Ordena os pares se sorted_pairs for True
    if sorted_pairs:
        pairs = [tuple(sorted(pair)) for pair in pairs]
        pairs.sort()
    return pairs
# Exemplo de utilização
array = [5, 7, 4, 3, 2]
result = pairs_with_smallest_difference(array, allow_duplicates=False, sorted_pairs=True, unique_pairs=True)
print(result)  # Output: [(2, 3), (3, 4), (4, 5)]