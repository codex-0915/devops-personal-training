#!/usr/bin/env python3

# Sample Problems with Regex

import re


def check_web_address(text):
  """ 
  Checks if the text passed qualifies as a valid top-level web address.
  
  The pattern to match is as follows:
  - A string that contains alphanumeric characters (which includes letters, numbers, and underscores), 
    as well as periods, dashes, and a plus sign, 
  - Followed by a period and a character-only top-level domain 
    such as ".com", ".info", ".edu", etc.
  
  Parameters:
  text (str): The string to check
  
  Returns:
  bool: True if the string is a valid top-level web address, False otherwise.
  """
  pattern = r"^[a-zA-Z][a-zA-Z0-9_.+-]+\.[a-zA-Z0-9-.]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


def check_time(text):
  """
  Checks if the given text matches the pattern of a valid 12-hour clock time format.

  The pattern to match is as follows:
  - An hour, which can be a single digit (1-9) or two digits (10-12).
  - A colon ':' followed by two digits between 00 and 59 representing minutes.
  - An optional space character.
  - A case-insensitive period of the day indicator, either 'AM', 'am', 'PM', or 'pm'.

  Parameters:
  text (str): The string to check
  
  Returns:
  bool: True if the string is a valid 12-hour time format, False otherwise.
  """
  pattern = r"^(1[0-2]|[1-9]{1}):([0-5][0-9])( ?)(am|pm|AM|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


def contains_acronym(text):
  """
  Checks if the given text matches the pattern of containing an acronym.

  The pattern to match is as follows:
  - An opening parenthesis '('.
  - A sequence of characters starting with an uppercase letter and followed by any number of alphanumeric characters.
  - A closing parenthesis ')'.

  Parameters:
  text (str): The string to check

  Returns:
  bool: True if the string contains an acronym, False otherwise.
  """
  pattern = r'\(([A-Z][A-Za-z0-9]*|[a-z0-9][A-Za-z0-9]*)\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


def correct_function(text):
  """
  Checks if the given text matches the pattern of containing a valid zip code.

  The pattern to match is as follows:
  - A space followed by five digits.
  - Or, five digits followed by a hyphen and four digits.

  Parameters:
  text (str): The string to check

  Returns:
  bool: True if the string contains a valid zip code, False otherwise.
  """
  result = re.search(r"( \d{5}|\d{5}-\d{4})", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  """
  Checks if the given text matches the pattern of containing a valid zip code.

  Calls the correct_function helper function to check if the text matches the pattern.

  Parameters:
  text (str): The string to check

  Returns:
  bool: True if the string contains a valid zip code, False otherwise.
  """
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

