import convert_decimals_to_fractions

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
