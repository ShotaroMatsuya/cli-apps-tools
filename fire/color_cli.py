import fire
from termcolor import colored, cprint


def greet(name, age, gender):
    print(
        colored(
            "Hello {} you are {}".format(name, age), "red", "on_blue", attrs=["reverse"]
        )
    )
    cprint("You are a {}".format(gender), "blue", "on_white")


def say_bye(name):
    print("Good bye {}".format(name))


if __name__ == "__main__":
    fire.Fire({"greet": greet, "saybye": say_bye})
