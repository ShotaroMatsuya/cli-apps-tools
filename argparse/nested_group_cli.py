import argparse


def main():
    """A Simple nested command CLI"""

    # Init/Main Parser
    parser = argparse.ArgumentParser(
        description="A Simple Nested CLI", prog="nested_group"
    )

    # Sub Parser/Sub Cmd
    subparsers = parser.add_subparsers(help="Sub Commands")

    # Subcommand
    list_parser = subparsers.add_parser("list", help="List all contents")
    list_parser.add_argument("dirname", help="Your Directory")

    create_parser = subparsers.add_parser("create", help="create a file")
    create_parser.add_argument("--read-only", help="Create A Read Only file")

    # NameSpace Storage
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
