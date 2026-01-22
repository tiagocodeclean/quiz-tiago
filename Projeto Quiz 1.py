print("Seja muito bem vindo ao Quiz do Tiago!")
answer_user = input("Quer Começar? (S/N) ")

if answer_user.upper() == "N":
    print("ta bom não vamos jogar hoje")
    quit()
elif answer_user.upper() != "S":
    quit()

print("Vamos Começar!")
import time
for i in [3, 2, 1]:
    print(i)
    time.sleep(1)

print("Pergunta 1: Qual a capital do Brasil?")
answer_1 = input(
    "a) São Paulo\n"
    "b) Rio de Janeiro\n"
    "c) Brasília\n"
    "d) Salvador\n"
    "Resposta: \n"
)
if answer_1 == "c":
    print("Resposta correta!\n")
else:
    print("Resposta errada! A resposta correta é (C) Brasília.\n") 

print("Pergunta 2: Qual o maior planeta do sistema solar?")
answer_2 = input(
    "a) Terra\n"
    "b) Júpiter\n"
    "c) Saturno\n"
    "d) Marte\n"
    "Resposta: "
)
if answer_2 == "b":
    print("Resposta correta!")
else:
    print("Resposta errada! A resposta correta é (B) Júpiter.\n")

print("Pergunta 3: Quem é o maior ladrão do Brasil'?")
answer_3 = input(
    "a) Luladrao\n"
    "b) Tiririca\n"
    "c) Silvio Santos\n"
    "d) Chaves\n"
    "Resposta: "
)   
if answer_3 == "a":
    print("Resposta correta!Ele é um Safado mesmo!")
else:
    print("Resposta errada! A resposta correta é (A) Luladrao.")        