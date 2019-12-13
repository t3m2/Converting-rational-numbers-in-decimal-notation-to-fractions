"""
Author: @t3m2.
Date: 9,10/07/2019, (july), dd/mm/yyyy.
Language: Python.

This program converts rational numbers into fractions,
I have built the function from_string_to_fraction()
that receives a string representing a rational number
in decimal notation, such as "2.5(37)", "-7.8" or "4"
and returns a string with the correspondent fraction.

Eg.: from_string_to_fraction("-2.5(37)") returns "-1256/495". 

It needs the functions gcd() and number_of_decimal_places_of()!

This only works with rational numbers because rational numbers
are all the numbers and the only numbers that can be written as
the divison of two integers, that's the definition of rational numbers.
Note that recurring decimals are rational numbers, and that 0,(9)=1.

Read the functions' docstrings for more information.
"""

def gcd(a=1, b=1):
  """Returns the greatest common divisor
  between two positive integers. 
  (Recursive solution)
  
  Make sure a and b are positive int's 
  because this function assumes that."""
  if b == 0:
    return a 
  else: 
    return gcd(b, a%b)


def number_of_decimal_places_of(x=0):
  """Returns the number of decimal places of a float.
  
  Make sure x is a float or int
  because this function assumes that."""
  if x == int(x):
    return 0
  return len(str(x)[str(x).index('.')+1:])


def from_string_to_fraction(x='0'):
  """Receives a string representing a rational number in decimal notation,
  such as "-2.5(37)", "-7.8" or "4",
  and returns a string with the correspondent fraction. 
  
  Eg.: from_string_to_fraction("-2.5(37)") returns "-1256/495".
  
  It needs the functions gcd() and number_of_decimal_places_of()! 
  
  Make sure that: (input restrictions)
  - the argument is a valid string representing
    a rational number in decimal notation;
  - the decimal separator (if there) is a '.' or a ',';
  - if the input is a recurring decimal, the period comes between round brackets.
  Because this function assumes that!"""
  
  # The input string can have a ',' or a '.' separating the int and the decimal part:
  x = x.replace(',', '.', 1)  
  
  sign = 1 
  if x[0] == '-':  
    # iff x represent a negative number, this turns x into
    # a string representing positive number,
    # because if it easier to work with positives numbers.
    # And, in the end, we turn the result into negative again
    # by making something like: "final_result*=sign".
    sign = -1
    x = x[1:]

  ### Getting the finit part (f) and the period (p): ###

  # I will explain this with an example:
  # If x == "2.5(37)"; then I set f, the finit part, to 2.5 and p, the period, to 37.
  # If the number is non-recurring, f = x, since it has no period.
  # Eg: if x == "-3.4"; then f = -3.4 and p = 0.
  # Note that x, our argument, is still a 'string'.

  try:  # This will be executed iff x is a non-recurring decimal:
    f = eval(x)  # eval(x) "turns" the string x into a float or int.
    p = 0
  except TypeError:  # This will be executed iff x is a recurring decimal:
    f = float(x[:x.index('(')])  # The finit part of the dizim is all the way until '('.

    p = int(x[x.index('(')+1:x.index(')')])  # The period of the dizim is 
    # the part of the number between '(' and ')').

  ### Getting the numerator and denominator: ###

  # With f and p defined, I have to discover the numerator and the denominator:
  
  # Here is a method that can be used in order to discover the fraction:
  # If y=2,5(37): (mathematical notation)
  # 1000y - y = 2537,(37) - 25,(37)                   <=>
  # <=> y = ( 2537,(37)-25,(37) )    /     (1000-1)   <=>
  # <=> y =      (2537-25)           /     (1000-1)    =>
  #  => y =      numerator           /    denominator
  # Note that both numerator and denominator are integers.

  # I implemented this with f and p:

  numerator = f*10**(number_of_decimal_places_of(f)+len(str(p)))+p \
              - f*10**number_of_decimal_places_of(f) 

  denominator = 10**(number_of_decimal_places_of(f)+len(str(p))) \
                - 10**number_of_decimal_places_of(f)

  ### Simplifying the fraction: ###

  # Here I am slimplifying the fraction, if it's possible:

  factor = gcd(numerator, denominator)

  # "sign*" is used to get the correct sign of the final answer, 
  # ie, the same sign of x.
  numerator = sign*(numerator/factor)
  denominator = denominator/factor

  return "%d/%d" % (numerator, denominator) 


### TESTING ###

print("This program turns \"any\" rational number in decimal notation \
into a fraction, for example: -2.5(37) = -2.537373737373737... = -1256/495\n\n")

while 1:
  try:
    x = input("Enter a rational number in decimal notation (exit: 'b'): ")
    if x == 'b':
      break
    print("%s = %s" % (x, from_string_to_fraction(x)))
  except:
    print("Error: probably, invalid input.")

  print()
