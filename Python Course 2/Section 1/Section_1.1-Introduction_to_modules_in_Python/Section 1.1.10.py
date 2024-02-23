# 1.1.10 SECTION QUIZ

# Question 1: You want to invoke the function make_money() contained in the module named mint.
# Your code begins with the following line:
import mint
# What is the proper form of the function's invocation?

# ANSWER ----------------
mint.make_money()

# Question 2: You want to invoke the function make_money() contained in the module named mint.
# Your code begins with the following line
from mint import make_money
# What is the proper form of the function's invocation?

# ANSWER--------
make_money()

# Question 3: You've written a function named make_money on your own. You need to import a function of
# the same name from the mint module and don't want to rename any of your previously defined names.
# Which variant of the import statement may help you with the issue?

# ANSWER ----------
from mint import make_money as make_more_money

# Question 4: What form of the make_money function invocation is valid if your
# code starts with the following line?
from mint import *

# ANSWER -------------
make_money()



