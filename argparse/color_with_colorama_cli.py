import argparse

from colorama import Back, Fore, Style, init


def main():
    parser = argparse.ArgumentParser(description="Working with Colors")

    # optional args
    parser.add_argument("--firstname", "-f", help="Your First Name")

    args = parser.parse_args()

    print("Hello {}".format(args.firstname))

    print(Fore.BLUE, "Hello {}".format(args.firstname))
    print(Style.RESET_ALL)
    print("Hello {} [without color]".format(args.firstname))

    print(Fore.MAGENTA, Back.BLACK, "Hello {}".format(args.firstname))
    print(Style.DIM)
    print(Style.RESET_ALL)


if __name__ == "__main__":
    main()
