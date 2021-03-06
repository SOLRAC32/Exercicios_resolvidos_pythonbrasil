"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
# SOLUÇÃO 01

ano_entrada = 1996
aumento = 0.015
salario_inicial = 1_000
salario_atual = salario_inicial
while True:
    try:
        ano_atual = int(input('Digite o ano atual: '))
        if ano_atual > 1996:
            break
    except ValueError:
        print('Você digitou um valor inválido, tente novamente.')

for _ in range(1997, ano_atual + 1, 1):
    salario_atual = salario_atual * (1 + aumento)
    aumento = aumento * 2

print(f'O salário atual do funcionário é de {"%.2f" % salario_atual} RS')
