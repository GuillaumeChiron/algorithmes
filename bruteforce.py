import csv

with open("csv/liste_d'actions.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for ligne in reader:
        print(
            ligne["Actions #"],
            ligne["Coût par action (en euros)"],
            ligne["Bénéfice (après 2 ans)"],
        )
