#!/usr/bin/env python3

def double_letters(string):
    last_letter = ""
    for letter in string:
        if last_letter == "":
            last_letter = letter
            continue
        if letter == last_letter:
            return True
        last_letter = letter
    return False


def test_double_letters_hello_string():
    #GIVEN
    string = "hello"
    #WHEN
    result = double_letters(string)
    #THEN
    assert result == True

def test_double_letters_nono_string():
    #GIVEN
    string = "nono"
    #WHEN
    result = double_letters(string)
    #THEN
    assert result == False
