# -*- coding: utf-8 -*-

"""
HomeWork Task 2
"""

import collections
import re


WORD_WHITESPACES_CLEAR_PATTERN = re.compile(r'\W')

def palindrome_verify(word: str) -> bool:
    """Verify if a word is a palindrome

    :param word: given word or phrase (string)
    :return True if a palindrome (boolean)
    """

    # Clear of any non-word characters
    word = re.sub(WORD_WHITESPACES_CLEAR_PATTERN, '', word)
    # Convert to lower case
    word = word.casefold()
    if len(word) < 2:
        return False

    # Init deque with word
    d = collections.deque()
    d.extend(list(word))

    # Verification
    while len(d) > 1:
        if d.popleft() != d.pop():
                return False

    # Word is palindrome
    return True
