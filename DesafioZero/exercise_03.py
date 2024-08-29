def all_subsets(nums):
    subsets = [[]]
    for num in nums:
        subsets += [curr + [num] for curr in subsets]
    return subsets
# Exemplo de utilização
nums = [1, 2]
result = all_subsets(nums)
print(result)  # Output: [[], [1], [2], [1, 2]]