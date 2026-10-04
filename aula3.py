# if== se
# elif== senão, se
# else== se não
#== é igual a
#> é maior que
#< é menor que
#  >= é maior ou igual a
#  <= é menor ou igual a
#!= é diferente de
#Objetivo:
# 1- Quero o nome do aluno
# 2- Quero a idade do aluno
# 3- Quero o valor da mensalidade padrão
# 4- Se a idade for menor que 21 anos, aplica 15% de desconto na mensalidade
# 5- Se a idade for igual a 21 anos e menor que 25 anos , aplica 10% de desconto na mensalidade
# 6- Se não atender a nenhum dos critérios acima, não aplica desconto na mensalidade

nome= str( input ( "qual o seu nome?: " ))
idade= int( input ( "qual a sua idade?: " ))
mensalidade= float( input ( "qual o valor da mensalidade?: R$" ))
if idade < 21:
    desconto= mensalidade  * 0.15
    nova_mensalidade= mensalidade - desconto
elif idade >= 21 and idade < 25:
    desconto= mensalidade * 0.10
    nova_mensalidade= mensalidade - desconto
else:
    nova_mensalidade= mensalidade
if idade < 21:
    promocao= "15%"
elif idade >= 21 and idade < 25:
    promocao= "10%"
else:
    promocao= "0%"
print (f"Olá {nome}, sua idade é {idade} anos e o valor da sua mensalidade com desconto {promocao} é R${nova_mensalidade:.2f}.")