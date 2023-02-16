import argparse


def main():
    parser = argparse.ArgumentParser(description="Mutually Exclusive Options")

    parser.add_argument("number", type=int)

    # Mutually Exclusive Option
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--verbose", "-v", help="Verbosely Process Task", action="store_true"
    )
    group.add_argument(
        "--quiet", "-q", help="Silently Process Task", action="store_true"
    )

    args = parser.parse_args()

    result = args.number * 40
    # print(result)

    if args.verbose:
        print("The multiplication result of {} : {}".format(args.number, result))
    elif args.quiet:
        print(">>", result)
    else:
        print(result)


if __name__ == "__main__":
    main()
