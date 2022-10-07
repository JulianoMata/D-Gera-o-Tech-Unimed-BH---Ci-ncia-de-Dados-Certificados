contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Se 'chave' já existir o valor é atualizado
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

# Caso não exista a 'chave', esta e seu valor são adicionados
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
