import csv


# Fonction qui permet de récupérer les données d'un fichier csv et retourner une liste de ces données
def load_actions(csv_file):
    list_actions = []

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for l in reader:

            rendement = float(l["Bénéfice (après 2 ans)"].replace("%", ""))
            profit = float(l["Coût par action (en euros)"]) * (rendement / 100)

            list_actions.append(
                {
                    "action": l["Actions #"],
                    "price": int(l["Coût par action (en euros)"]),
                    "profit": profit,
                }
            )

    return list_actions


# Affiche les meilleures actions, le meilleur coût et le meilleur profit
def display_result_optimized(best_profit, best_cost, best_combo):

    print(
        f"{best_combo}\n"
        f"L'achat des {len(best_combo)} actions, pour un cout total de {best_cost}€ a generé {round(best_profit, 2)}€ de profit"
    )


# Affiche les combinaisons théoriques,les combinaisons testées, les valeur du cout, du profit ainsi que la liste avec les meilleures action achetées
def display_result_bruteforce(
    total_possibilities, count, best_profit, best_cost, best_combo
):

    print(
        f"Combinaisons théoriques : {total_possibilities}\n"
        f"Combinaisons testées : {count}\n"
        f"Le meilleur profit est de {round(best_profit, 2)}€, pour un cout de {best_cost}€\n"
        f"Liste des actions: {best_combo}"
    )
