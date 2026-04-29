def resolver_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Disco 1: {origem} ➔ {destino}")
        return
    resolver_hanoi(n - 1, origem, auxiliar, destino)
    

    print(f"Disco {n}: {origem} ➔ {destino}")
    
    resolver_hanoi(n - 1, auxiliar, destino, origem)

# Execução
n_discos = 3
print(f"Resolvendo para {n_discos} discos:")
resolver_hanoi(n_discos, 'Haste A', 'Haste C', 'Haste B')

total_movimentos = 2**n_discos - 1
print(f"\nTotal de movimentos: {total_movimentos}")
