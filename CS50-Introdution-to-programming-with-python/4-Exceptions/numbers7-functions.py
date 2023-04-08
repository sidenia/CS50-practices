def main():
  x = get_int()
  print(f"X is {x}")


def get_int():
  while True:
    try:
      return int(input("What's x? "))
    except ValueError:
      pass

if __name__ == "__main__":
  main()