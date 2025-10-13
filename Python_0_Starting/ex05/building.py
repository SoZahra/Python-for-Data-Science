import sys

def main():
    """ Progamme qui compte le nb de caracteres d'un texte"""
    if len(sys.argv) > 2:
        print("AssertionError")
        return
    elif len(sys.argv) == 1:
       texte = input("What is the text to count?\n") + '\n'
    else:
        texte = sys.argv[1]
    upper = 0
    lower = 0
    ponctuation = 0
    spaces = 0
    digits = 0
    total = 0

    for char in texte:
        if char.isupper():
            upper = upper + 1
        elif char.islower():
            lower = lower + 1
        elif char.isspace():
            spaces = spaces + 1
        elif char.isdigit():
            digits = digits + 1
        elif not char.isalnum() and not char.isspace():
            ponctuation = ponctuation + 1
    total = upper + lower + spaces + digits + ponctuation
    print(f"The text contains {total} characters:\n" f"{upper} upper letters\n" f"{lower} lower letters\n" f"{ponctuation} punctuation marks\n" f"{spaces} spaces\n" f"{digits} digits")
       


if __name__ == "__main__":
  main()