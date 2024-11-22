# FizzBuzz

Your mission is to write a program that implements FizzBuzz.

FizzBuzz rules
-------------------------
Given a number:
- If the number is divisible by `3`, return `Fizz`.
- If the number is divisible by `5`, return `Buzz`.
- If the number is divisible by both `3` and `5`, return `FizzBuzz`.
- Otherwise, return the number unmodified.

### Examples
`1` -> `1`  
`2` -> `2`  
`3` -> `Fizz`  
`4` -> `4`  
`5` -> `Buzz`  
...  
`14` -> `14`  
`15` -> `FizzBuzz`  
`16` -> `16`  
`17` -> `17`  
`18` -> `Fizz`

Requirements
-------------------------
1. If no parameters are provided: 
   * Print all numbers from 1 to 100 (inclusive), following the rules of FizzBuzz
   * Output one number per line  
   ```
   python fizzbuzz.py
   ```

2. If a single numerical parameter is provided:
   * Print the provided number, following the rules of FizzBuzz  
   ```
   python fizzbuzz.py 21
   ```


### Extra challenges
1. If the flag `--even` is passed in, numbers that are divisible by `3` AND are **even** should print `EvenFizz` instead of `Fizz`
    ```
   python fizzbuzz.py 12 --even
    ```

2. Accept an arbitrary string as the parameter. Print the string, applying FizzBuzz to any numbers within the string.  
    ```
   python fizzbuzz.py "3 may keep a secret, if 2 of them are dead."
    ```
   
3. Apply FizzBuzz to any numbers written as text
    ```
   python fizzbuzz.py "Three may keep a secret, if two of them are dead."
   python fizzbuzz.py "Twenty-five"
    ```
