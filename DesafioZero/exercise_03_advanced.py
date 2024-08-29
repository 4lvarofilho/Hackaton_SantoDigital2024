from itertools import combinations

def all_subsets(nums, max_size=None, min_size=None, distinct_only=False, sort_subsets=False):
    # Gera todos os subsets possíveis
    subsets = [[]]
    for num in nums:
        subsets += [curr + [num] for curr in subsets]
    # Filtra subsets por tamanho mínimo e máximo
    if max_size is not None:
        subsets = [s for s in subsets if len(s) <= max_size]
    if min_size is not None:
        subsets = [s for s in subsets if len(s) >= min_size]
    # Remove subsets com elementos duplicados se distinct_only for True
    if distinct_only:
        subsets = [list(set(s)) for s in subsets]
    # Ordena os subsets e seus elementos se sort_subsets for True
    if sort_subsets:
        subsets = [sorted(s) for s in subsets]
        subsets.sort()
    return subsets
# Exemplo de uso
nums = [1, 2]
result = all_subsets(nums, max_size=2, min_size=0, distinct_only=True, sort_subsets=True)
print(result)  # Output: [[], [1], [2], [1, 2]]