def main():
  hello("world")
  goodbye("World")


def hello(name):
  print(f'Hello, {name}')


def goodbye(name):
  print(f'Goodbye, {name}')


#it will just execute main when you call the file saying directly
if __name__ == '__main__':
  main()