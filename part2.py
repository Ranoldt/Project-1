def question1(n: dict) -> dict:
    return {value: key for key, value in n.items()}


def question2(n: dict) -> dict:
    return {value: [key for key in n if n[key] == value] for value in n.values()}


def question3(n1: dict, n2: dict) -> dict:
    return {key: (n1[key] if key in n1 else 0) + (n2[key] if key in n2 else 0) for key in set(list(n1) + list(n2))}


def question4(n: list) -> list:
    return list({element for element in [element for sublist in n for element in sublist] if [element for sublist in n for element in sublist].count(element) > 1})
