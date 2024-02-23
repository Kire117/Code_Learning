# 1.2.6 Selected functions from the platform module

# The platform function
# The platform module lets you access the underlying platform's data, i.e., hardware, operating system,
# and interpreter version information.
#
# There is a function that can show you all the underlying layers in one glance, named platform, too.
# It just returns a string describing the environment; thus, its output is rather addressed to humans
# than to automated processing (you'll see it soon).
#
# This is how you can invoke it:

# platform(aliased = False, terse = False)

# And now:
#
# aliased → when set to True (or any non-zero value) it may cause the function to present
# the alternative underlying layer names instead of the common ones;
# terse → when set to True (or any non-zero value) it may convince the function to present a briefer
# form of the result (if possible)

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

# The machine function
# Sometimes, you may just want to know the generic name of the processor which runs your OS together
# with Python and your code - a function named machine() will tell you that. As previously,
# the function returns a string.
#
# Again, we ran the sample program:

from platform import machine

print(machine())

# The processor function
# The processor() function returns a string filled with the real processor name (if possible).
#
# Once again, we ran the sample program:

from platform import processor

print("Processor:" + processor())
# The system function
# A function named system() returns the generic OS name as a string.

from platform import system

print("System:", system())

# The version function
# The OS version is provided as a string by the version() function.

from platform import version


print("Version:", version())

from platform import python_implementation, python_version_tuple

print("Python Implementation: "+python_implementation())

for atr in python_version_tuple():
    print("ATR (version_tuple) " + atr)
















