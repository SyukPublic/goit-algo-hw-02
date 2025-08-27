# -*- coding: utf-8 -*-

"""
Tests for Task 2
"""

from tasks import palindrome_verify


def main():
    try:

        while True:
            try:
                if palindrome_verify(input("\nEnter the word: ")):
                    print("The word entered is a palindrome")
                else:
                    print("he word entered is not a palindrome")

                user_input = input("\nDo you want to continue? [Y/n]: ")
                if user_input.lower() == 'n':
                    break
            except (EOFError, KeyboardInterrupt):
                break

        print("\nGood bye!")

    except Exception as e:
        print(e)

    exit(0)


if __name__ == "__main__":
    main()
