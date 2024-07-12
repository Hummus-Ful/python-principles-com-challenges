#!/usr/bin/env python3

def add_dots(string):
    """This function takes a string and adds "." in between each letter"""
    new_string = ""
    for char in string:
        new_string = new_string + char + "."
    
    return new_string.rstrip(".")  # remove the last "." and return

def remove_dots(string):
    """This function removes all dots from a string"""
    new_string = ""
    for char in string:
        if char == ".":
            continue
        new_string = new_string + char
    return new_string


def test_add_dots():
    #GIVEN
    string = "test"
    #WHEN
    result = add_dots(string)
    #THEN
    assert result == "t.e.s.t"

def test_remove_dots():
    #GIVEN
    string = "t.e.s.t"
    #WHEN
    result = remove_dots(string)
    #THEN
    assert result == "test"
