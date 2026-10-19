def validar_senha(senha):
    if len(senha) <= 3:
        return 'Senha deve possuir mais de 3 caracteres.'
    elif len(senha) > 100:
        return 'Por favor, digite uma senha menor que 100 caracteres.'
    else:
        return 'Senha Válida.'
