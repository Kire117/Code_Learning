# 1.2.3 Is there real randomness in computers?

# A random number generator takes a value called a seed, treats it as an input value, calculates a "random" number
# based on it (the method depends on a chosen algorithm) and produces a new seed value.

# 1.2.4 Selected functions from the random module

# The random function
# The most general function named random() (not to be confused with the module's name)
# produces a float number x coming from the range (0.0, 1.0) - in other words: (0.0 <= x < 1.0).

# The example program below will produce five pseudorandom values -
# as their values are determined by the current (rather unpredictable) seed value, you can't guess them:

from random import random

print("Random function")
for i in range(5):
    print(random())

# The seed function
# The seed() function is able to directly set the generator's seed. We'll show you two of its variants:
#
# seed() - sets the seed with the current time;
# seed(int_value) - sets the seed with the integer value int_value.
# We've modified the previous program - in effect, we've removed any trace of randomness from the code:

from random import random, seed

print("\nSeed function")
seed(0)

for i in range(5):
    print(random())

# The randrange and randint functions
# If you want integer random values, one of the following functions would fit better:
#
# randrange(end)
# randrange(beg, end)
# randrange(beg, end, step)
# randint(left, right)
# The first three invocations will generate an integer taken (pseudorandomly) from the range (respectively):
#
# range(end)
# range(beg, end)
# range(beg, end, step)
# Note the implicit right-sided exclusion!
#
# The last function is an equivalent of randrange(left, right+1) - it generates the integer value i,
# which falls in the range [left, right] (no exclusion on the right side).
#
# Look at the code in the editor. This sample program will consequently output a line consisting
# of three zeros and either a zero or one at the fourth place.

print("The randrange and randint functions")

from random import randrange, randint

print("\nfirst:", randrange(1), end=' ')
print("\nSecond:", randrange(0, 1), end=' ')
print("\nThird:", randrange(0, 1, 1), end=' ')
print("\nFourth:", randint(0, 1))

# Another example
print("\nAnother example")
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

# The choice and sample functions

# As you can see, this is not a good tool for generating numbers in a lottery. Fortunately, there is a better
# solution than writing your own code to check the uniqueness of the "drawn" numbers.
#
# It's a function named in a very suggestive way - choice:
#
# choice(sequence)
# sample(sequence, elements_to_choose)
# The first variant chooses a "random" element from the input sequence and returns it.
#
# The second one builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence.
#
# In other words, the function chooses some of the input elements, returning a list with the choice.
# The elements in the sample are placed in random order. Note: the elements_to_choose must not be greater
# than the length of the input sequence.
#
# Look at the code below:

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

