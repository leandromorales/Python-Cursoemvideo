
def valor(msg):
    n = None
    while True:
        n = input(msg).replace(',', '.')
        try:
            n = float(n)
            break
        except ValueError:
                print(f'\033[0;31mERRO! \"{n}\" é um valor inválido.\033[m')
    return n
