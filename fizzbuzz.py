import sys
import re

from word2number import w2n


def fizzbuzz_single(number, even_flag=False):
    """Apply FizzBuzz rules to a single number."""
    result = ""
    if number % 3 == 0:
        result += "Fizz"
        if even_flag and number % 2 == 0:
            result = "EvenFizz"  # Override with EvenFizz if even flag is set
    if number % 5 == 0:
        result += "Buzz"
    return result or str(number)


def fizzbuzz_range(even_flag=False):
    """Generate FizzBuzz for numbers 1 to 100."""
    return "\n".join(
        fizzbuzz_single(i, even_flag=even_flag) for i in range(1, 101)
    )


def fizzbuzz_in_string(input_string, even_flag=False):
    """Apply FizzBuzz to numbers embedded in a string."""
    def replace_numeric(match):
        num = int(match.group())
        return fizzbuzz_single(num, even_flag=even_flag)

    def replace_word(match):
        word: str = match.group().lower()
        word = word.replace(' ', " ")
        try:
            numerical = w2n.word_to_num(word)
            fizzbuzzed = fizzbuzz_single(numerical, even_flag=even_flag)
            if fizzbuzzed.isdigit():
                return match.group()
            else:
                return fizzbuzz_single(numerical, even_flag=even_flag)
        except ValueError as e:
            return match.group()  # Return the original word if not a number word

    input_string = re.sub(r'\b\d+\b', replace_numeric, input_string)
    return re.sub(r'\b[\w-]+\b', replace_word, input_string)


def main():
    args = sys.argv[1:]

    if not args:
        # No input: Generate full range FizzBuzz
        print(fizzbuzz_range())
        return

    even_flag = "--even" in args
    args = [arg for arg in args if arg != "--even"]  # Remove the flag

    if len(args) == 1:
        arg = args[0]
        # Strip single or double quotes around strings
        arg = arg.strip("'\"")

        if re.match(r'^\d+$', arg):  # Single numerical input
            print(fizzbuzz_single(int(arg), even_flag=even_flag))
        else:  # any string
            print(fizzbuzz_in_string(arg, even_flag=even_flag))

    else:
        print("Usage: target_script.py [input] [--even]")


if __name__ == "__main__":
    main()
