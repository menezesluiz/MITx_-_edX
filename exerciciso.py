"""
Será criado um programa para cadastro de frequentadores da fabem.
"""

nome = input("Nome: ")
idade = int(input("Idade: "))
email = input("e-mail: ")
cidade = input("Cidade: ")
telefone = input("Telefone de contato: ")

print(f"O seu nome é: {nome}, sua idade é: {idade}, seu e-mail é: {email},"
      f"sua cidade é: {cidade}, e seu telefone é: {telefone}?. Podemos,"
      f"confirmar?")