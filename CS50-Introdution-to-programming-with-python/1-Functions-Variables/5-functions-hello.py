#using fuctions 

def main():
  hello('Sidenia')


def hello(name):
  name = input("What's your name? ").strip().title()
  print(f"Hello, {name}")


if __name__ == '__main__':
  main()