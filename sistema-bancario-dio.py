# documentação: https://academiapme-my.sharepoint.com/:p:/g/personal/kawan_dio_me/Ef-dMEJYq9BPotZQso7LUCwBJd7gDqCC2SYlUYx0ayrGNQ?rtime=FoYGrZuE20g

import os

LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500
saldo = 0
total_saques_realizados = 0
saques = []
depositos = []

print(f'''
{" BEM-VINDO AO BANCO DIO! ".center(100, "#")}
''')

while True:
    print()
    print(f'''DIGITE UMA DAS SEGUINTES OPÇÕES:

[1] DEPOSITAR
[2] SACAR
[3] VER EXTRATO

[0] SAIR

''')
    
    opcao_escolhida = input("| ")
    print()

    os.system("clear")
    if opcao_escolhida == "1":
        print("VOCÊ ESCOLHEU A OPÇÃO: DEPÓSITO".center(50, "="))
        quantia_a_depositar = input("DIGITE A QUANTIA QUE DESEJA DEPOSITAR: R$ ")

        try:
            quantia_a_depositar = float(quantia_a_depositar)
            if quantia_a_depositar < 0:
                print("APENAS VALORES POSITIVOS. TENTE NOVAMENTE")
                continue
            saldo += quantia_a_depositar
            depositos.append(quantia_a_depositar)
        except ValueError:
            print("DIGITE APENAS NUMEROS. TENTE NOVAMENTE")

    elif opcao_escolhida == "2":
        print("VOCE ESCOLHEU A OPÇÃO: SAQUE".center(50, "="))
        quantia_a_sacar = input("DIGITE A QUANTIA QUE DESEJA SACAR: R$ ")
        try:
            quantia_a_sacar = float(quantia_a_sacar)
            
            if quantia_a_sacar < 0:
                print("DIGITE APENAS NUMEROS POSITIVOS. TENTE NOVAMENTE")
                continue
            elif (total_saques_realizados >= LIMITE_SAQUES_DIARIOS) or \
            (quantia_a_sacar > 500.00):
                print("VOCE JÁ ATINGIU O LIMITE DE SAQUES OU TENTOU SACAR MAIS DE R$ 500. TENTE NOVAMENTE MAIS TARDE")
                continue
            elif (quantia_a_sacar > saldo):
                print("VOCE TENTOU SACAR MAIS DO QUE O SALDO DISPONIVEL NA CONTA. TENTE NOVAMENTE")
                continue
            
            total_saques_realizados +=1
            saques.append(quantia_a_sacar)
            saldo -= quantia_a_sacar
        except ValueError:
            print("DIGITE APENAS NUMEROS. TENTE NOVAMENTE")
        

    elif opcao_escolhida == "3":
        print("DEPOSITOS REALIZADOS:")
        for valor in depositos:
            print(f"R$ {valor:.2f}")
        print()

        print("SAQUES REALIZADOS:")
        for valor in saques:
            print(f"R$ {valor:.2f}")
        print()

        print(f"VALOR NA CONTA: R$ {saldo:.2f}")
        print()

    elif opcao_escolhida == "0":
        print('SAINDO...')
        print("VOLTE SEMPRE!!")
        break
    else:
        print("OPÇÃO NÃO ENCONTRADA. TENTE NOVAMENTE")