# Crie uma função para validar o tamanho de um nome de usuário (receba o nome).
# Retorna verdadeiro caso o nome tenha mais que 5 caracteres

def validar_nome(nome_usuario):
    if len(nome_usuario) > 5:
        return True
    else:
        return False

print(validar_nome('Breno')) # false
print(validar_nome('Vinicius')) #true

    