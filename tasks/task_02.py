# -*- coding: utf-8 -*-

"""
HomeWork Task 2
"""

import collections
import re


WORD_WHITESPACES_CLEAR_PATTERN = re.compile(r'\W')

def palindrome_verify(text: str) -> bool:
    """
    Verify if a word is a palindrome

    :param text: given word or phrase (string)
    :return True if a palindrome (boolean)
    """

    # Clear of any non-word characters
    text = re.sub(WORD_WHITESPACES_CLEAR_PATTERN, '', text)
    # Convert text to lower case
    text = text.casefold()
    if len(text) < 2:
        return False

    # Init deque with word
    d = collections.deque()
    d.extend(list(text))

    # Verification
    while len(d) > 1:
        if d.popleft() != d.pop():
                return False

    # Text is palindrome
    return True
