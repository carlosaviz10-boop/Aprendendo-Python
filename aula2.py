#Quero o nome do usuário
#o ano de nascimento dele
# O valor da mensalidade da faculdade dele
# quanto ele pagará no total por 12 meses dessa mensalidade
#Exibir uma mensagem no final bem organizada no terminal , mostrando o nome do aluno, a idade calculada para 2026 e o custo total anual da faculdade.
nome= str(input("qual o seu nome?:"))
ano= int(input("Em que ano você nasceu?: "))
idade= 2026 - ano
valor= float(input("Qual o valor de sua mensalidade?:R$"))
total= 12 * valor
print(f"Como vai {nome} ? Você tem ou terá {idade} anos em 2026 e pagará um total de R${total:.2f} em 12 meses de mensalidade da faculdade.")