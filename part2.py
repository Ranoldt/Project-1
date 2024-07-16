def question1(n: dict) -> dict:
    return {value: key for key, value in n.items()}


def question2(n: dict) -> dict:
    return {value: [key for key in n if n[key] == value] for value in n.values()}


def question3(n: dict, m: dict) -> dict:
    return {key: n.get(key, 0) + m.get(key, 0) for key in list(n) + list(m)}

def question4(n: list) -> list:
    return list({element for sublist in n for element in sublist})