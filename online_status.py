#!/usr/bin/env python3

def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == "online":
            count = count+1
    return count 


def test_online_count():
    #GIVEN
    input = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    #WHEN
    output = online_count(input)
    #THEN
    assert output == 2
