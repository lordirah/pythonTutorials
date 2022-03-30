from functools import cached_property


class t:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Acts like an attribute
    @property
    def s(self):
        print("Inside property")
        return self.x + self.y

    # Runs only once for that instance
    @cached_property
    def u(self):
        print("Inside cached property")
        return self.x + self.y


if __name__ == "__main__":
    t1 = t(2, 3)
    print(t1.s)
