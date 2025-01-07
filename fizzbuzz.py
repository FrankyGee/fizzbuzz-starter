import sys


def apply_fizzbuzz(number: str|int) -> str:
    pass


def fizzbuzz_range() -> str:
    pass


def main():
    args = sys.argv[1:]

    if not args:
        # No input: Generate full range FizzBuzz
        print(fizzbuzz_range())
        return
    else:
        for number in args:
            print(f"{number} -> {apply_fizzbuzz(number)}")
    print("HELP HELP I'M TRAPPED IN THE KERNEL")


if __name__ == "__main__":
    main()
