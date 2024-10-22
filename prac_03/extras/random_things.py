"""Random Boolean Generator."""

import random

PASS_THRESHOLD = 50
TAX_THRESHOLD = 18200  # as of 2024


def main():
    """Generate three boolean values."""
    print(is_heads())
    print(is_pass(random.uniform(0, 100)))
    print(has_tax(random.randrange(10000, 50000, 1000)))


def is_heads():
    """Flip a coin."""
    return random.randint(0, 1) == 1


def is_pass(score):
    """Determine if score is greater than or equal to PASS_THRESHOLD."""
    if score < 0 or score > 100:
        print("Invalid Value: Outside Range 0 to 100.")
        return False
    else:
        return score >= PASS_THRESHOLD


def has_tax(income):
    """Determine if income is greater than minimum TAX_THRESHOLD."""
    return income > TAX_THRESHOLD


main()
