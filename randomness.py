#!/usr/bin/env python3

import random

def random_number():
    return random.randint(1, 100)


def test_random_number():
    #GIVEN
    low = 1
    high = 100
    #WHEN
    rand_num = random_number()
    #THEN
    print(rand_num)  # print to console using `pytest -s` command
    assert rand_num >= low
    assert rand_num <= high