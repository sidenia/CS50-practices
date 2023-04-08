# for i in [0,1,2]:
#   print('meow')

# for i in range(3):
#   print('meow')

# # when you dont care about the variable, and its just for a kinda sintaxe of the language you can use this convention _
# for _ in range(3):
#   print('meow')

# print("meow\n" * 3, end="")

# while True:
#   n = int(input("What's n?"))
#   if n < 0:
#     continue
#   else:
#     print('n=',n)
#     break

while True:
  n = int(input("What's n?"))
  if n > 0:
    break

for _ in range(n):
  print("meow")