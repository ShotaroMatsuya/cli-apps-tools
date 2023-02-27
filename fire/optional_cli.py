import fire


def greet(name, age, gender):
    print("Hello {} you are {}".format(name, age))
    print("You are a {}".format(gender))


def say_bye(name):
    print("Good bye {}".format(name))


if __name__ == "__main__":
    fire.Fire({"greet": greet})
