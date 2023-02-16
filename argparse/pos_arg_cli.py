import argparse


def main():
    # Init
    parser = argparse.ArgumentParser()

    # Positional Argument
    # Mandatory
    # without --

    parser.add_argument("firstname", help="Your firstname first")
    parser.add_argument("lastname", help="Your lastname last")

    # Namespace Storage
    args = parser.parse_args()
    print(args)
    print(
        "your firstname is {} and your surname is {}".format(
            args.firstname, args.lastname
        )
    )


if __name__ == "__main__":
    main()
