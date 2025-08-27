# -*- coding: utf-8 -*-

"""
Tests for Task 1
"""

import random

from tasks import generate_request, process_request


def main():
    try:

        while True:
            try:
                # Create and enqueue requests
                for _ in range(random.randint(1, 10)):
                    generate_request()
                # Dequeue and process requests
                for _ in range(random.randint(1, 10)):
                    process_request()

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
