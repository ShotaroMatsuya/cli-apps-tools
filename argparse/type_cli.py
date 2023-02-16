import argparse


def main():
    """A Simple CLI with Argparse"""
    # Constructor/Init
    parser = argparse.ArgumentParser(
        prog="basiccli",
        description="A simple cli with argparse",
        epilog="Additional Description",
    )

    # Version
    parser.add_argument("--version", "-v", version="%(prog)s 0.01", action="version")

    # Options Arg

    parser.add_argument("--firstname", "-f", help="First Name", type=str)
    parser.add_argument("--age", "-a", help="Your Age", default=20, type=int)
    parser.add_argument("--gender", "-g", help="Your Gender", dest="sex")
    parser.add_argument("--salary", "-s", help="Your salary", type=float)
    parser.add_argument(
        "--jobtype", "-ht", help="Your Job Type", choices=("Remote", "Full-Time")
    )

    # Stores Args
    args = parser.parse_args()
    print(type(args))
    print("Hello {} type:: {}".format(args.firstname, type(args.firstname)))
    print("Hello your age is {} type:: {}".format(args.age, type(args.age)))
    print("Hello your gender is {} type:: {}".format(args.sex, type(args.sex)))
    sum_salary = 40 + args.salary
    print("Your salary is {} type:: {}".format(args.salary, type(args.salary)))
    print("Sum of salary", sum_salary)
    print("You are a {} worker".format(args.jobtype))


if __name__ == "__main__":
    main()
