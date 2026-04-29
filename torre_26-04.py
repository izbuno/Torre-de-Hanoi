def resolver_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Disco 1: {origem} ➔ {destino}")
        return

    resolver_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Disco {n}: {origem} ➔ {destino}")
    resolver_hanoi(n - 1, auxiliar, destino, origem)

discos = int(input("Número de discos: "))

print(f"\nResolvendo para {discos} discos:")
resolver_hanoi(discos, 'Haste A', 'Haste C', 'Haste B')

print(f"\nTotal de movimentos: {2**discos - 1}")
