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
        
        extrato.append("D: +" + str(valor_deposito))
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
            
            extrato.append("S: -" + str(valor_saque))
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

    def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
        usuarios.append({
            "usuario" : (len(usuarios) + 1),
            "nome" : nome,
            "data_de_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco})

    def criar_conta_corrente(cpf_usuario):
        contas_corrente.append({
            "cpf_usuario" : cpf_usuario,
            "num_conta" : (len(contas_corrente) + 1),
            "agencia" : "0001"
        })
        ...
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE = 500
    saldo = 0
    total_saques_realizados = 0
    saques = []
    depositos = []
    extrato = []
    usuarios = []
    contas_corrente = []

    print(f'{" BEM-VINDO AO BANCO DIO! ".center(100, "#")}')


    while True:
        print()
        print('DIGITE UMA DAS SEGUINTES OPÇÕES:\n[1] DEPOSITAR\n[2] SACAR\n[3] VER EXTRATO\n[4] CADASTRAR USUARIO\n[5] CRIAR CONTA CORRENTE\n[0] SAIR\n')
        
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
            
            saque_final = sacar(valor_saque=quantia_a_sacar)
            total_saques_realizados +=1 if saque_final != 0 else 0
            saldo -= saque_final
            
            

        elif opcao_escolhida == "3":
            mostrar_extrato(extrato)

        elif opcao_escolhida == "4":
            print("VOCE ESCOLHEU A OPÇÃO: CADASTRAR USUÁRIO")

            nome = input("DIGITE O NOME DO USUARIO: ").strip()
            data_nascimento = input("DIGITE A DATA DE NASCIMENTO: ").strip()
            cpf = input("DIGITE O CPF: ").replace("-", "").replace(".", "").strip()
            endereco = input("DIGITE O ENDERECO (logradouro - num - bairro - cidade/estado sigla): ").strip()

            cpf_cadastrado = False
            for usuario in usuarios:
                if cpf == usuario["cpf"]:
                    cpf_cadastrado = True
                    break

            if cpf_cadastrado:
                print("USUARIO JÁ CADASTRADO. TENTE NOVAMENTE")
                continue
            
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        
        elif opcao_escolhida == "5":
            print("VOCE ESCOLHEU A OPÇÃO: CRIAR CONTA CORRENTE")
            print()

            cpf_usuario = input("DIGITE O CPF DO USUARIO DA CONTA: ").replace("-", "").replace(".", "").strip()

            
            for usuario in usuarios:
                if cpf_usuario == usuario["cpf"]:
                    criar_conta_corrente(cpf_usuario)
                    break
                else:
                    print("USUARIO NAO ENCONTRADO. TENTE NOVAMENTE")
            
            
            

        elif opcao_escolhida == "0":
            print('SAINDO...')
            print("VOLTE SEMPRE!!")
            break
        else:
            print("OPÇÃO NÃO ENCONTRADA. TENTE NOVAMENTE")

if __name__ == "__main__":
    main()