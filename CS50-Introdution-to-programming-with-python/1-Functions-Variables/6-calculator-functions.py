def main():
  x = int(input("What's x?"))
  print("x squared is", square(x))

def square(n):
  return n * n


# def square(n):
#   return n ** 2


# def square(n):
#   return pow(n, 2)

if __name__ == '__main__':
  main()