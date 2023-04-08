# #EX01 INTEGER
# x = input('Whats x value?')
# y = input('Whats y value?')
# z = int(x) + int(y)
# print(z)


# #EX02 INTEGER
# x = int(input('Whats x value?'))
# y = int(input('Whats y value?'))
# print(x + y)


# #EX03 FLOAT
# x = float(input('Whats x value?'))
# y = float(input('Whats y value?'))
# print(x + y)


# #EX04 FLOAT - ROUND WITH CODE SYNTAX
# x = float(input('Whats x value?'))
# y = float(input('Whats y value?'))
# z = x + y
# print(f'{z:,}') # separa milhar, milhao com virgula


# #EX05 FLOAT - USING ROUND METHOD
# x = float(input('Whats x value?'))
# y = float(input('Whats y value?'))
# z = round(x / y, 2)
# print(z) # separa milhar, milhao com virgula


#EX05 FLOAT - USING ROUND METHOD
x = float(input('Whats x value?'))
y = float(input('Whats y value?'))
z = x / y
print(f'{z:.2f}') # separa milhar, milhao com virgula com f string passando quantos dígitos se quer

