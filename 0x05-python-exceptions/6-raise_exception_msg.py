#!/usr/bin/python3
try:
    raise_exception_msg("This is a name error")
except NameError as e:
    print(e)
