#!/usr/bin/env python3

def only_ints(param1, param2):
    if type(param1) is int and type(param2) is int:
        return True 
    return False


def test_only_ints_two_ints():
    #GIVEN
    i1 = 1
    i2 = 2
    #WHEN
    result = only_ints(i1, i2)
    #THEN
    assert result == True

def test_only_ints_int_and_float():
    #GIVEN
    i = 4
    f = 2.1
    #WHEN
    result = only_ints(i, f)
    #THEN
    assert result == False

def test_only_ints_int_and_char():
    #GIVEN
    i = 1
    c = "a"
    #WHEN
    result = only_ints(i, c)
    #THEN
    assert result == False

def test_only_ints_int_and_bool():
    #GIVEN
    i = 1
    b = True
    #WHEN
    result = only_ints(i, b)
    #THEN
    assert result == False