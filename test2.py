phrase = "Un chasseur sachant chasser sans son chien n'est pas un vrai chasseur"


def max_and_min_words(string: str) -> str:
    liste = string.split(" ")
    max_word = max(liste, key=len)
    min_word = min(liste, key=len)

    return max_word, min_word


max_word, min_word = max_and_min_words(phrase)

print(f"Le mot le plus long est: {max_word}\nLe mot le plus court est: {min_word}")
