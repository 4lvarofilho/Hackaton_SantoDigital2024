def generate_stars(n):
    star_list = []
    for i in range(1, n + 1):
        star_list.append('*' * i)
    return star_list
# Exemplo de utilização da função generate_stars
n = 5
result = generate_stars(n)
print(result)