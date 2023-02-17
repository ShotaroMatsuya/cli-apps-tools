import fire


class Calc(object):
    def __init__(self, x, y):
        """A Simple Calc CLI"""
        super(Calc, self).__init__()
        self.x = x
        self.y = y

    # Fxn Add
    def add(self):
        """Add Numbers"""
        return self.x + self.y

    # Fxn Subtract
    def subtract(self):
        """Subtract Numbers"""
        return self.x - self.y

    # Fxn Multiple
    def multiply(self):
        """Multiply Numbers"""
        return self.x * self.y

    # Fxn Divide
    def divide(self):
        """Divide Numbers"""
        return self.x / self.y


if __name__ == "__main__":
    fire.Fire(Calc)
