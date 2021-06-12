"""A welcome code special for you."""
import argparse


HELLO = (
    "Hello, {name}! Congratulations for starting your journey "
    "in data science.\nMy name is Syahrul Bahar Hamdani, "
    "but just call me Dani for short.\n"
    "Together for the next few weeks, we will learn a lot.\n"
    "From learning how to code with Python, "
    "to using Python to solve data science problem.\n"
    "Let's get started!!"
)


def main():
    parser = argparse.ArgumentParser(
        description="A welcome drink (read: script) for you."
    )
    parser.add_argument("yourname", action="store", type=str,
                        help="write your name wrapped in a double-quotes")
    args = parser.parse_args()
    print(HELLO.format(name=args.yourname))


if __name__ == "__main__":
    main()
