#!/usr/bin/env python3

def capital_indexes(string):
    lst = []
    index = 0
    for letter in string:
        if letter.isupper():
            lst.append(index)
        index = index+1
    return lst



def test_capital_indexes():
    # GIVEN
    input = "HeLlO"
    # WHEN
    output = capital_indexes(input)
    # THEN
    assert output == [0, 2, 4]