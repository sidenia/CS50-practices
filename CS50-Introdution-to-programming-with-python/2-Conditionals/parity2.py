"""
+  -  *  /  %
"""
def main():
  x = int(input("What's x?"))

  if is_even(x):
    print('Even')
  else:
    print('Odd')


# def is_even(n):
#   if n % 2 == 0:
#     return True

# def is_even(n):
#   return True if n % 2 == 0 else False

def is_even(n):
  #it will return true if n % 2 == 0
  return n % 2 == 0

main()