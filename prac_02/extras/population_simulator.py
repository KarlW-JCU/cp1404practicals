"""
Population simulation program
"""

from random import uniform

MINIMUM_BIRTHS = 0.10
MAXIMUM_BIRTHS = 0.20
MINIMUM_DEATHS = 0.05
MAXIMUM_DEATHS = 0.25


def main():
    """Get species name and initial population then simulate for 10 years."""
    population = []
    species = input('Species Name: ').title()
    print(f"Welcome to the {species} Population Simulator!")
    population.append(int(input('Starting Population: ')))
    print(population)
    for i in range(0, 10):
        print(f"Year {i + 1}")
        births = round(uniform(MINIMUM_BIRTHS, MAXIMUM_BIRTHS) * population[i])
        deaths = round(uniform(MINIMUM_DEATHS, MAXIMUM_DEATHS) * population[i])
        print(f"{births} {species} were born. {deaths} died.")
        population.append(population[i] + births - deaths)
        print(f"Population: {population[i]}.")


main()
