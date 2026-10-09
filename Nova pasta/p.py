#1- Peça um número para o usuário e diga se ele é par ou ímpar
num = float(input("digite um numero: "))
if num % 2 == 0:
  print("o numero é par")
else:
  print("o numero é impar")
#2- Peça um número par ao usuário e diga se ele é positivo, negativo ou zero
num1 = float(input("digite um numero par: "))
if num > 0:
  print("o numero é positivo")
elif num == 0:
  print("o numero e zero")
elif num < 0:
  print("o numero e negativo")

#3- Peça um usuário e senha. Se o usuário for 'admin' E a senha for '1234', mostre 'Acesso liberado', se não mostre 'Acesso negado'
us = (input("digite seu usuario: "))
senha = float(input("digite sua senha: "))
if us == 'admin' and senha == 1234:
 print("acesso liberado")
else:
  print("aceso negado")
#4- Peça uma idade e informe a categoria: criança(até 11), adolescente(12 a 17), adulto(18 a 59), idoso(60 ou mais)
idade = float(input("digite sua idade: "))

if idade >= 0 and idade <= 11:
    print("crianca")
elif idade >=12 and idade <=17 :
  print("adolescente")
elif idade >= 18 and idade <= 59:
  print("adulto")
elif idade >= 60:
  print("idoso")