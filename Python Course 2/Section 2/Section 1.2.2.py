# 1.2.2 Selected functions from the math module


# Let's start with a quick preview of some of the functions provided by the math module.

# We've chosen them arbitrarily, but that doesn't mean that the functions we haven't mentioned here are any less
# significant. Dive into the modules' depths yourself - we don't have the space or the time to talk about everything
# in detail here.

# The first group of the math's functions are connected with trigonometry:

# sin(x) → the sine of x;
# cos(x) → the cosine of x;
# tan(x) → the tangent of x.
# All these functions take one argument (an angle measurement expressed in radians) and return the appropriate result
# (be careful with tan() - not all arguments are accepted).

# Of course, there are also their inversed versions:

# asin(x) → the arcsine of x;
# acos(x) → the arccosine of x;
# atan(x) → the arctangent of x.
# These functions take one argument (mind the domains) and return a measure of an angle in radians.

# To effectively operate on angle measurements, the math module provides you with the following entities:

# pi → a constant with a value that is an approximation of π;
# radians(x) → a function that converts x from degrees to radians;
# degrees(x) → acting in the other direction (from radians to degrees)

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)  # True
print(ar == pi / 2.)  # True
print(sin(ar) / cos(ar) == tan(ar))  # True
print(asin(sin(ar)) == ar)  # True

# Apart from the circular functions (listed above) the math module also contains a set of their hyperbolic analogues:
#
# sinh(x) → the hyperbolic sine;
# cosh(x) → the hyperbolic cosine;
# tanh(x) → the hyperbolic tangent;
# asinh(x) → the hyperbolic arcsine;
# acosh(x) → the hyperbolic arccosine;
# atanh(x) → the hyperbolic arctangent.

# Another group of the math's functions is formed by functions which are connected with exponentiation:
#
# e → a constant with a value that is an approximation of Euler's number (e)
# exp(x) → finding the value of ex;
# log(x) → the natural logarithm of x
# log(x, b) → the logarithm of x to base b
# log10(x) → the decimal logarithm of x (more precise than log(x, 10))
# log2(x) → the binary logarithm of x (more precise than log(x, 2))
# Note: the pow() function:
#
# pow(x, y) → finding the value of xy (mind the domains)
# This is a built-in function, and doesn't have to be imported.

from math import e, exp, log
print("\nanother math group example")
print(pow(e, 1) == exp(log(e)))  # True
print(pow(2, 2) == exp(2 * log(2)))  # True
print(log(e, e) == exp(0))  # True

# The last group consists of some general-purpose functions like:
#
# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
# floor(x) → the floor of x (the largest integer less than or equal to x)
# trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
# factorial(x) → returns x! (x has to be an integral and not a negative)
# hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y
# (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)
# Look at the code in the editor. Analyze the program carefully.
#
# It demonstrates the fundamental differences between ceil(), floor() and trunc().
print("Last group example")

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
