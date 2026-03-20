tableau = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]

for i, index in enumerate(tableau):
    total_ligne = 0
    for j in index:
        total_ligne += j
    print(f"Ligne: {i} -> {total_ligne}")
