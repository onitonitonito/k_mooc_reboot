"""
# Simple Decorator type TEST!
#
"""
# print(__doc__)


def main():
    names = ['Kay', 'Suparx', 'the cat person']
    ingredients = ['Meat', 'Water', 'Salt', 'Pepper']
    # names = ['Kay',]
    greeting = "Good morning!"

    [show_greeting(name) for name in names]
    [show_situation(name, greeting) for name in names]
    show_repeated_ingredient_args(ingredients)

def deco(func):
    def inner(*args):
        repeat = 4

        if len(args) is 1:
            attatch =" "
            args_str = f"'{args[0]}'"

        elif len(args) is 2:
            repeat = 9
            attatch = f"& say '{args[1]}'.."
            args_str = f"'{args[0]}', '{args[1]}'"

        else:
            attatch = " "
            args_str = ", ".join(list(*args))

        print(f"* {func.__name__}({args_str})")
        print("=====" * repeat)

        func(*args)

        print("-----" * repeat)
        print(f"Wave hand~ {attatch} ")
        print("\n")

        if len(args) > 1:
            return args[1]
        else:
            return None
    return inner


@deco
def show_greeting(name):
    print(f"Hello~ '{name}'!...")


@deco
def show_situation(name, greeting):
    print(f"When you bump into '{name}' in the street..")


@deco
def show_repeated_ingredient_args(*args):
    echoes = ""
    for arg in args:
        echoes += f"{i}.{arg}\n"


if __name__ == '__main__':
    main()
