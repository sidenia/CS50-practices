def main():
  x = get_int()
  print(f"X is {x}")


def get_int():
  while True:
    try:
      x = int(input("What's x? "))
      return x
    except ValueError:
      pass
    # except ValueError:
    #   print("x is not a number")

if __name__ == "__main__":
  main()