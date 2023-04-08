# #option 1 - NOME INSERIDO NA LINHA ABAIXO DA PERGUNTA
# print("What's your name?")
# name = input()
# print("Hello, " + name)

#option 2 - NOME INSERIDO NA LINHA DA PERGUNTA
name = input("What's your name? ")
print("Hello, " + name)
print("Hello,", name)

#usando f string
print(f"Hello, {name}")

#usando PRINT e sobrepondo comportamento para next line com o end=''
print("Hello,", end='')
print(name)