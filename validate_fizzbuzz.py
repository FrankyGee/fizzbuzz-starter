
import subprocess
# Define test cases with inputs and expected outputs
TEST_CASES = test_cases = [
    # Test 1: No input
    {
        "name": "No input",
        "input": [],
        "expected": "\n".join(
            ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
             "Fizz" if i % 3 == 0 else
             "Buzz" if i % 5 == 0 else
             str(i) for i in range(1, 101)]
        )
    },
    # Test 2: Single numerical inputs
    {
        "name": "Single input",
        "input": ["3"],
        "expected": "Fizz"
    },
    {
        "name": "Single input",
        "input": ["5"],
        "expected": "Buzz"
    },
    {
        "name": "Single input",
        "input": ["15"],
        "expected": "FizzBuzz"
    },
    {
        "name": "Single input",
        "input": ["7"],
        "expected": "7"
    },
    {
        "name": "Single input",
        "input": ["0"],
        "expected": "FizzBuzz"
    },
    # Test 3: Strings containing numerical numbers
    {
        "name": "String input",
        "input": ["'I have 3 apples and 5 oranges'"],
        "expected": "I have Fizz apples and Buzz oranges"
    },
    {
        "name": "String input",
        "input": ["'Numbers: 15, 2, and 3'"],
        "expected": "Numbers: FizzBuzz, 2, and Fizz"
    },
    # Test 4: Single numerical inputs with `--even` flag
    {
        "name": "Even Fizz",
        "input": ["6", "--even"],
        "expected": "EvenFizz"  # 6 is even and divisible by 3
    },
    {
        "name": "Even Fizz",
        "input": ["15", "--even"],
        "expected": "FizzBuzz"  # 15 is not even, standard rules apply
    },
    {
        "name": "Even Fizz",
        "input": ["4", "--even"],
        "expected": "4"  # 4 is not divisible by 3 or 5
    },
    {
        "name": "Even Fizz",
        "input": ["'Numbers: 30, 2, and 6'", "--even"],
        "expected": "Numbers: EvenFizzBuzz, 2, and EvenFizz"
    },
    # Test 5: Short strings containing numbers as words
    {
        "name": "Number words",
        "input": ["'Three, five, fifteen, and twenty-five are the numbers'"],
        "expected": "Fizz, Buzz, FizzBuzz, and Buzz are the numbers"
    },
    {
        "name": "Number words",
        "input": ["'Four and two are not FizzBuzz'"],
        "expected": "Four and two are not FizzBuzz"  # No FizzBuzz rules applied
    },
    {
        "name": "Number words",
        "input": ["'Six, and thirty are the numbers'"],
        "expected": "Fizz, and FizzBuzz are the numbers"
    },
    {
        "name": "Number words",
        "input": ["'Zero, you monster'"],
        "expected": "FizzBuzz, you monster"
    },
    # Test 6: Short strings containing numbers as words with `--even` flag
    {
        "name": "Number words with --even",
        "input": ["'Five, six, eleven, and thirty are the numbers'", "--even"],
        "expected": "Buzz, EvenFizz, eleven, and EvenFizzBuzz are the numbers"
    },
    # Test 7: Mix of numerical and word numbers
    {
        "name": "Mix of numerical and word numbers",
        "input": ["'6, 7, eight, and thirty are the numbers'"],
        "expected": "Fizz, 7, eight, and FizzBuzz are the numbers"
    },
    # Test 8: Strings without any numbers
    {
        "name": "Bereft of numbers",
        "input": ["'Hello there, friend'"],
        "expected": "Hello there, friend"
    }
]

def run_tests(script_path, test_cases):
    """
    Runs a series of tests on a given script and checks outputs against expected results.

    :param script_path: Path to the script to test.
    :param test_cases: A list of dictionaries containing 'input' and 'expected' keys.
    """
    for i, test_case in enumerate(test_cases):
        inputs = test_case.get("input")
        expected = test_case.get("expected")
        name = test_case.get("name")

        # Run the script using subprocess
        try:
            result = subprocess.run(
                ["python", script_path, *inputs],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            output = result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Test '{name}' failed to execute: {e.stderr.strip()}")
            continue

        # Compare actual output to expected output
        if output == expected:
            print(f"Test '{name}' PASSED")
        else:
            print(f"Test '{name}' FAILED")
            print(f"  Input: {inputs}")
            print(f"  Expected: {expected}")
            print(f"  Got: {output}")


if __name__ == "__main__":
    # Path to the script to be tested
    script_to_test = "fizzbuzz.py"

    # Run the tests
    run_tests(script_to_test, TEST_CASES)
