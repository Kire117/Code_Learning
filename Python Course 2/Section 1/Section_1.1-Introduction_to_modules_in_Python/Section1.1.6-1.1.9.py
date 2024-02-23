# 1.1.6 Importing a module: *
# from module import *


# 1.1.7 The as keyword Aliasing causes the module to be identified under a different name than the original. This may
# shorten the qualified names, too.
#
# Creating an alias is done together with importing the module, and demands the following form of the import
# instruction:

# import module as alias

# 1.1.8 Aliasing

# If you need to change the word math, you can introduce your own name, just like in the example:
import math as m

print(m.sin(m.pi / 2))

# In turn, when you use the from module import name variant and you need to change the entity's name, you make an
# alias for the entity. This will cause the name to be replaced by the alias you choose.

# This is how it can be done:

# from module import name as alias

# The phrase name as alias can be repeated - use commas to separate the multiplied phrases, like this:

# from module import n as a, m as b, o as c

from math import pi as PI, sin as sine

print(sine(PI / 2))

# Section Summary

# 1. If you want to import a module as a whole, you can do it using the import module_name statement. You are allowed
# to import more than one module at once using a comma-separated list. For example:


# import mod1  If you want to import a module as a whole, you can do it using the import module_name statement.
# import mod2, mod3, mod4

# If a module is imported in the above manner and you want to access any of its entities, you need to prefix
# the entity's name using dot notation. For example:

# import my_module
# result = my_module.my_function(my_module.my_data) The snippet makes use of two entities coming from the my_module
# module: a function named my_function() and a variable named my_data. Both names must be prefixed by my_module.

# The most general form of the above statement allows you to import all entities offered by a module:
#
#
# from my_module import *
#
# result = my_function(my_data)

# You can change the name of the imported entity "on the fly" by using the as phrase of the import. For example:
#
#
# from module import my_function as fun, my_data as dat
#
# result = fun(dat)

