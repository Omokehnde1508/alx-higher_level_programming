#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)
try:
  raise_exception_msg("This is a custom message for the exception")
except NameError as e:
  print(e)
