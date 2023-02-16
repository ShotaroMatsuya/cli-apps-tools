import argparse


def main():
    """A Simple CLI with Argparse"""
    # Constructor/Init
    parser = argparse.ArgumentParser(
        prog="basiccli",
        description="A simple cli with argparse",
        epilog="Additional Description",
        # allow_abbrev=False,
    )

    # Version
    parser.add_argument("--version", "-v", version="%(prog)s 0.01", action="version")

    # Options Arg

    parser.add_argument("--firstname", "-f", help="First Name")
    parser.add_argument("--age", "-a", help="Your Age", default=20)
    parser.add_argument("--gender", "-g", help="Your Gender", dest="sex")
    # Stores Args
    args = parser.parse_args()
    print(type(args))
    print("Hello {}".format(args.firstname))
    print("Hello your age is {}".format(args.age))
    print("Hello your gender is {}".format(args.sex))


if __name__ == "__main__":
    main()
