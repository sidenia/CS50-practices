def main():
    name = input("whats your name? ")
    print(hello(name)) # printing instead of just calling the fuction hello(name), which had a print inside


def hello(to="world"):
    # print("hello,", to) #the test doesnt work with this, bc you're not  returning anything
    return f"hello, {to}" # return the string instead of printting hello.


if __name__ == "__main__":
    main()