import argparse


def main():
    """A Simple CLI with Argparse"""

    # Init/Constructor
    parser = argparse.ArgumentParser(
        prog="opt_arg", description="A Simple CLI for Variable Argument"
    )

    # Optional Argument
    parser.add_argument("--firstname", "-f", help="Your Firstname")
    parser.add_argument("--salary", "-s", help="Your Salary", nargs=2)
    parser.add_argument("--city", "-c", help="Your City", nargs="+")
    parser.add_argument("--job", "-l", help="Your Jobs", nargs="?")
    # Multiple Variables
    parser.add_argument("--wages", "-w", help="Your Wages", nargs="*")

    # Variable Argument
    # ? = 0 or 1
    # + = all and atleast one
    # * = 0 or all
    # numb

    # Store Arg in Namespace
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
