nome = input("Qual seu nome [min 4 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo (use 'f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres, tente novamente: ")

while (idade < 0) or (idade > 150):
    idade = int(input("informe a idade entre 0 e 150: "))

while (salario<0):
    salario = float(input("Digite um salário válido ('acima de 0'): "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Valor inválido, digite 'f' ou 'm': ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Não entendeu? aqui vai uma legenda: 's'- solteiro, 'c'- casado, 'v'- viúvo e 'd'- divorciado")
    civil = input("Vamos tentar novamente, lembre de usar 's', 'c', 'v' ou 'd': \n")