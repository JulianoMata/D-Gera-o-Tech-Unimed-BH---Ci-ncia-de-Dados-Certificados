nome = "Juliano"
curso = "Python"

mensagem = f'''
    Olá, meu nome é \033[1;31m{nome}\033[m.
Estou revendo {curso}.
        Mensagem com diferentes recuos.
'''
print(mensagem)


print("""
      \033[1;31m============ MENU ============\033[m
      
      \033[1;32m[1] Depositar\033[m
      \033[1;33m[2] Sacar\033[m
      \033[1;34m[3] Sair\033[m
      
      \033[1;31m==============================\033[m
      
     \033[1;35;42mObrigado por usar nosso sistema!!!\033[m
      """)
