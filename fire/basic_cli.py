import fire


def greet(name):
    print("Hello {}".format(name))


def say_bye(name):
    print("Good Bye {}".format(name))


age = 24


class Employee(object):
    """docstring for Employee"""

    def __init__(self, name):
        super(Employee, self).__init__()
        self.name = name

    def __repr__(self):
        print("Employee(name={})".format(self.name))


if __name__ == "__main__":
    # fire.Fire()  # Exposes Every Component
    # fire.Fire(greet)  # Exposes A Single Fxn
    # fire.Fire(Employee)  # Exposes A Single Class
    fire.Fire({"greet": greet, "saybye": say_bye})
