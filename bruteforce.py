import csv

actions = []
action_cost = []
benef = []
rentability = []

with open("csv/liste_d'actions.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for l in reader:
        actions.append(l["Actions #"])
        action_cost.append(int(l["Coût par action (en euros)"]))
        benef.append(l["Bénéfice (après 2 ans)"])


client = 500

for i in range(20):

    benefice = int(benef[i].replace("%", "")) / 100
    renta = 1 + benefice
    rentability.append(renta)

rentability.sort(reverse=True)
print(rentability)

for a in range(20):
    action_client = rentability[a] * action_cost[a]
    print(action_client)
