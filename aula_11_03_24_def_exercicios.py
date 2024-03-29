# -*- coding: utf-8 -*-
"""aula_11.03.24_def_exercicios

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_rznESaEmHYL98uEr121oTJfIYQn7DrF
"""

def gerar_digito_verificador_1(digitos):
# Implemente a lógica para validar o dígito verificador 1
  soma_prod = 0
  for n in range(9):
    soma_prod += (digitos[n]*(10-n))
  d1 = ((soma_prod *10)%11)%10
  return d1
def gerar_digito_verificador_2(digitos):
  soma = 0
  for n in range(10):
    soma += (digitos[n]*(11-n))
  d2 = ((soma*10)%11)%10
  return  d2
  #print(digitos)

def gerar_cpf(cpf):
  # Implemente a lógica para validar o CPF
  cpf_n = [int(d)for d in cpf]
  d1 = gerar_digito_verificador_1(cpf_n)
  cpf_n.append(d1)
  d2 = gerar_digito_verificador_2(cpf_n)
  cpf_n.append(d2)

  return (str(cpf_n[0]) + str(cpf_n[1]) + str(cpf_n[2]) + '.' +
         str(cpf_n[3]) + str(cpf_n[4]) + str(cpf_n[5]) + '.' +
         str(cpf_n[6]) + str(cpf_n[7]) + str(cpf_n[8]) + '-' +
         str(d1)+str(d2))
  #cpf_n.append(d1,d2)
  #cpf_st = [str(d) for d in cpf]


# Função principal para solicitar os 9 primeiros dígitos do CPF e gerar os 2 dígitos verificadores
def main():
  cpf9 =  input("Digite os primeiros 9 dígitos do CPF a ser gerado (apenas números): ")
  cpf = gerar_cpf(cpf9)
  print(f'CPF = {cpf}')
# Chamando a função principal
main()

