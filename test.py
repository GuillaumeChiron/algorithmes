def return_money(price):

    result = []

    for m in money:
        while price >= m:
            price -= m
            result.append(m)

    return result


price = int(input("Saisir un montant: "))
money = [50, 20, 10, 5, 2, 1]

result = return_money(price)
print(result)
