[![Run on Repl.it](https://repl.it/badge/github/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions)](https://repl.it/github/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions)
# Converting rational numbers in decimal notation to fractions
This repository contains a [Python](https://www.python.org/) program that converts strings representing [rational numbers](https://en.wikipedia.org/wiki/Rational_number), in [decimal notation](https://en.wikipedia.org/wiki/Decimal), to [fractions](https://en.wikipedia.org/wiki/Fraction_(mathematics)) in form "_n_/_m_" where _n_ and _m_ are [integers](https://en.wikipedia.org/wiki/Integer).

For example: -2.5(37) = -2.537373737373737... = -1256/495.

**This is particularly useful when we have a [repeating decimal](https://en.wikipedia.org/wiki/Repeating_decimal) and want to write it as a fraction.** For instance, the number 825.27(123) is equal to which fraction (in form _n_/_m_ where both _n_ and _m_ are integers)? You can [use the program to find out](https://github.com/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions/blob/master/main.py). 

This only works with rational numbers because [rational numbers](https://en.wikipedia.org/wiki/Rational_number) are all the numbers and the only numbers that can be written as the divison of two integers, that is the definition of rational numbers. Note that [recurring decimals](https://en.wikipedia.org/wiki/Repeating_decimal) (dízimas infinitas periódicas) are rational numbers, and that [0,(9)=1](https://en.wikipedia.org/wiki/0.999...).

I created the following files:
- [x] [*convert_decimals_to_fractions.py*](https://github.com/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions/blob/master/convert_decimals_to_fractions.py) where I defined the functions needed and **explained the process in the comments**;

- [x] [*main.py*](https://github.com/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions/blob/master/main.py)  which can be used to convert rational numbers (in decimal notation) to fractions by using *convert_decimals_to_fractions*;

- [x] [*.replit*](https://github.com/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions/blob/master/.replit) in which I "tell" [Repl.it](https://repl.it/) what to do if you [run this reposiotry on Repl.it](https://repl.it/github/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions). (Although I didn't have to, because the main program is called main.py);

- [x] [*README.md*](https://github.com/t3m2/Converting-rational-numbers-in-decimal-notation-to-fractions/blob/master/README.md), this file.

Note that [operation with floats are not exact](https://docs.python.org/2/tutorial/floatingpoint.html) so, approximations are a possibility, the program doesn't have infinite precision, and numbers that are too big or too small will be approximated or result in an error...
