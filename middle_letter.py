#!/usr/bin/env python3

def mid(string):
    if len(string)%2 == 0:
        return ""
    middle = len(string)/2
    middle = int(middle)
    return string[middle]
    

def test_mid_string_length_is_odd():
    #GIVEN
    input = "abc"
    #WHEN
    output = mid(input)
    #THEN
    assert output == "b"

def test_mid_string_length_is_even():
    #GIVEN
    input = "aaaa"
    #WHEN
    output = mid(input)
    #THEN
    assert output == ""
