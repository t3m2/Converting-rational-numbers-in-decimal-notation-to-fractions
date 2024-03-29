"""
Author: t3m2
Date: 9,10/7/2019, dd/mm/yyyy
Language: Python

This program tests the document convert_decimals_to_fractions.py.
It "asks" for rational numbers in decimal notation,
(including repeating decimals) and
prints the correspondent fraction in form n/m, 
where n and m are integers, until the user wants to exit.
"""

import convert_decimals_to_fractions
# Check convert_decimals_to_fractions.py for more information.

print("This program turns \"any\" rational number in decimal notation \
into a fraction, for example: -2.5(37) = -2.537373737373737... = -1256/495\n\n")

while 1:
  try:
    x = input("Enter a rational number in decimal notation (exit: 'b'): ")
    if x == 'b':
      break
    print("%s = %s" % (x, convert_decimals_to_fractions.from_string_to_fraction(x)))
  except:
    print("Error: probably, invalid input.")

  print()
