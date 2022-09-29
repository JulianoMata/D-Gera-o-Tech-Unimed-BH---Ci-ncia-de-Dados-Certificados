conta_normal= True
conta_universitaria = False
conta_especial: False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
   
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!")
   
    else:
        print("Saldo Insuficiente.")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    
    else:
        print("Saldo insuficiente")
        
elif conta_especial:
    print("Cliente Ouro!!!")

else:
    print("Sistema não reconheceu tipo de conta. Entre em contato com gerente.")