# Crie uma função que valida se uma senha do usuário é válida. Esta função deve receber
# uma string e retornar:
# · Se len(senha) <= 3 "Senha deve possuir mais de 3 caracteres!"
# · Se senha > 100 "Por favor digite uma senha menor que 100!"
# · Caso contrário retornar "Senha Válida!"
# . Extraia a função para outro arquivo (Exemplo: validacoes.py) e importe no arquivo
# principal

from validacao import validar_senha

print(validar_senha('12'))
print(validar_senha('123'))


