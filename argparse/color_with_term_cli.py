import argparse

from termcolor import colored, cprint


def main():
    parser = argparse.ArgumentParser(description="Working with Colors")

    # optional args
    parser.add_argument("--firstname", "-f", help="Your First Name")

    args = parser.parse_args()

    print("Hello {}".format(args.firstname))

    # Formular
    # colored(TEXT, fg,bg,attrs=[])
    # on_white
    # on_blue

    print(colored("Hello {}".format(args.firstname), "blue", "on_white"))
    cprint("Hello {}".format(args.firstname), "blue", "on_white")

    text = "Your firstname was {}".format(args.firstname)

    cprint(text, "green", "on_white", attrs=["blink"])
    cprint(text, "green", "on_white", attrs=["reverse"])
    cprint(text, "green", "on_white", attrs=["reverse", "blink"])


if __name__ == "__main__":
    main()
