def only_digits(cpf: str) -> str:
    numbers = ""
    for character in cpf:
        if character.isdigit():
            numbers = numbers + character
    return numbers


if __name__ == "__main__":
    print(only_digits("498.518.215-00"))
