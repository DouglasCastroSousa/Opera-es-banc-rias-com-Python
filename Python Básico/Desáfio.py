#       Desafio
# 
# Fomos contratatos por um grane banco para desenvolver o seu novo sistema.
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
# Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato. 

saldo = 0
limite_diario = 500
numero_saques = 0
limite_saques = 3
extrato =  ""

menu = """
========== MENU ==========

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

==========================

>> """
while True: 
    
    opção = input(menu)
    
    if opção == "1":
        valor = float(input("\nInforme um valor para depósito "))
        if valor >= 1:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
        else:
            print("Operação falhou! O valor informado é inválido!")
    elif opção == "2":
        valor = float(input("\nInforme um valor para saque "))
        if valor > saldo:
            print("Operação falhou! O valor excedo o tamanho do saldo!")
        elif valor > limite_diario:
            print("Operação falhou! O valor inserido excede o limite diário por saque")
        elif numero_saques >= limite_saques:
            print("Operação falhou! Número máximo de saques por dia atingido!")
            extrato += "Saque falho [limite diário de 3 saques atingido]"
        elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saques += 1
        else:
            print("Operação falhou, valor invalido")
            
    elif opção == "3":
        print("\n================ EXTRATO ================ \n")
        print("Não foram realizadas movintações") if extrato == "" else print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n ========================================= ")
        
    elif opção == "0":
        break
    else:
        print("Operação inválida, porfavor, selecione novamente! ")