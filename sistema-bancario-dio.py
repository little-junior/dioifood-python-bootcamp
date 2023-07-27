# documentação: https://academiapme-my.sharepoint.com/:p:/g/personal/kawan_dio_me/Ef-dMEJYq9BPotZQso7LUCwBJd7gDqCC2SYlUYx0ayrGNQ?rtime=FoYGrZuE20g

import os

def main():
    def depositar(valor_deposito):
        try:
            valor_deposito = float(valor_deposito)
            if valor_deposito < 0:
                print("APENAS VALORES POSITIVOS. TENTE NOVAMENTE")
                return 0
        except ValueError:
            print("DIGITE APENAS NUMEROS. TENTE NOVAMENTE")
            return 0
        
        extrato.append("+" + str(valor_deposito))
        return valor_deposito

    def sacar(valor_saque):
        try:
            valor_saque = float(valor_saque)
            
            if valor_saque < 0:
                print("DIGITE APENAS NUMEROS POSITIVOS. TENTE NOVAMENTE")
                return 0
            elif (total_saques_realizados >= LIMITE_SAQUES_DIARIOS) or \
            (valor_saque >= 500.00):
                print("VOCE JÁ ATINGIU O LIMITE DE SAQUES OU TENTOU SACAR MAIS DE R$ 500. TENTE NOVAMENTE MAIS TARDE")
                return 0
            elif (valor_saque > saldo):
                print("VOCE TENTOU SACAR MAIS DO QUE O SALDO DISPONIVEL NA CONTA. TENTE NOVAMENTE")
                return 0
            
            extrato.append("-" + str(valor_saque))
        except ValueError:
            print("DIGITE APENAS NUMEROS. TENTE NOVAMENTE")
            return 0
        
        return valor_saque

    def mostrar_extrato(extrato):
        print("============EXTRATO============")

        for i in extrato:
            print(i)

        print()
        print(f"VALOR NA CONTA: R$ {saldo:.2f}")
        print()



    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE = 500
    saldo = 0
    total_saques_realizados = 0
    saques = []
    depositos = []
    extrato = []


    print(f'{" BEM-VINDO AO BANCO DIO! ".center(100, "#")}')


    while True:
        print()
        print('DIGITE UMA DAS SEGUINTES OPÇÕES:\n[1] DEPOSITAR\n[2] SACAR\n[3] VER EXTRATO\n[0] SAIR\n')
        
        opcao_escolhida = input("| ")
        print()

        os.system("cls")
        if opcao_escolhida == "1":
            print("VOCÊ ESCOLHEU A OPÇÃO: DEPÓSITO".center(50, "="))
            quantia_a_depositar = input("DIGITE A QUANTIA QUE DESEJA DEPOSITAR: R$ ")

            deposito_final = depositar(quantia_a_depositar)
            saldo += deposito_final
                
        

        elif opcao_escolhida == "2":
            print("VOCE ESCOLHEU A OPÇÃO: SAQUE".center(50, "="))
            quantia_a_sacar = input("DIGITE A QUANTIA QUE DESEJA SACAR: R$ ")
            
            saque_final = sacar(quantia_a_sacar)
            total_saques_realizados +=1 if saque_final != 0 else 0
            saldo -= saque_final
            
            

        elif opcao_escolhida == "3":
            mostrar_extrato(extrato)

        elif opcao_escolhida == "0":
            print('SAINDO...')
            print("VOLTE SEMPRE!!")
            break
        else:
            print("OPÇÃO NÃO ENCONTRADA. TENTE NOVAMENTE")

if __name__ == "__main__":
    main()