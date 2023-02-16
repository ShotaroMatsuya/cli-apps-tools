import argparse


def main():
    parser = argparse.ArgumentParser(description="Customizing Groups CLI")

    # Optional Arg
    parser.add_argument("--firstname", "-f", help="Specify Your FirstName")

    # Positional Arg
    parser.add_argument("age", help="Specify your age", default=18)

    # Custom group Arg
    group = parser.add_argument_group("authentication")
    group.add_argument(
        "--user",
        "-u",
    )
    group.add_argument(
        "--password",
        "-p",
    )
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
