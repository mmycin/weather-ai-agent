from os import system, name

def clear() -> None:
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")