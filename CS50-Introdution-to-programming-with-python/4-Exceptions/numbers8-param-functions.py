def main():
  x = get_int("What's x?")
  print(f"X is {x}")


def get_int(param):
  while True:
    try:
      return int(input(param))
    except ValueError:
      pass

if __name__ == "__main__":
  main()