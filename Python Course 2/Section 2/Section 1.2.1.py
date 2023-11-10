# 1.2 Section 2 – Selected Python modules (math, random, platform)

# 1.2.1 Working with standard modules

# The function returns an alphabetically sorted list containing all entities' names available in the module
# identified by a name passed to the function as an argument:N

# dir(module)

# Note:if the module's name has been aliased, you must use the alias, not the original name.

# Using the function inside a regular script doesn't make much sense, but it is still possible.
# For example, you can run the following code to print the names of all entities within the math
# module:

import math

for name in dir(math):
    print(name, end=" ")


