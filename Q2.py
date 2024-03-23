def eh_fibonacci(num):
    t1 = 0
    t2 = 1
    while t1 <= num:
        if t1 == num:
            return True
        t1, t2 = t2, t1 + t2
    return False

numero_entrada = int(input('Informe um número: '))
if eh_fibonacci(numero_entrada):
    print(f'O número {numero_entrada} pertence à sequência de fibonacci.')
else:
    print(f'O número {numero_entrada} NÃO pertence à sequência de fibonacci')

        