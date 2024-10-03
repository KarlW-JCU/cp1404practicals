"""Random numbers program."""

import random

print(random.randint(5, 20))  # line 1
"""
What did you see on line 1?                         # 16
What was the smallest number you could have seen,   # 5
what was the largest?                               # 20
"""

print(random.randrange(3, 10, 2))  # line 2
"""
What did you see on line 2?                         # 3
What was the smallest number you could have seen,   # 3
what was the largest?                               # 9
Could line 2 have produced a 4?                     # no
"""

print(random.uniform(2.5, 5.5))  # line 3
"""
What did you see on line 3?                         # 4.380089390309932
What was the smallest number you could have seen,   # 2.5
what was the largest?                               # 5.5
"""

"""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
print(random.uniform(1, 100))
