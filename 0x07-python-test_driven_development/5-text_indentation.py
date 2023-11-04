#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    nchar = 0
    while nchar < len(text) and text[nchar] == " ":
        nchar += 1

    while nchar < len(text):
        print(text[nchar], end="")
        if text[nchar] == "\n" or text[nchar] in ".?:":
            if text[nchar] in ".?:":
                print("\n")
            nchar += 1
            while nchar < len(text) and text[nchar] == " ":
                nchar += 1
            continue
        nchar += 1
