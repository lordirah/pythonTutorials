import functools


def dec(a, b):
    def dec_decorator(func):
        @functools.wraps(func)
        def dec_inner(*args, **kwargs):
            print(a)
            ret = func(*args, **kwargs)
            print(b)
            return ret

        return dec_inner

    return dec_decorator


@dec("starting", "ending")
def f(x):
    print(x)


def main():
    f(1)
    c1 = C(1)
    print(c1.x)
    print(c1.y)
    c1.class_method()
    c1.static_method()
    C.class_method()
    C.static_method()


class C:
    def __init__(self, x):
        self.x = x

    @property
    def y(self):
        return self.x + 10

    @classmethod
    def class_method(cls):
        print("Inside class method")

    @staticmethod
    def static_method():
        print("Inside Static method")


if __name__ == "__main__":
    main()
