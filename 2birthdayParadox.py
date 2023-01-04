"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/bid-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumerOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumerOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date objects of a birthday that occurs more than once
    in the birthdat list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday.


# Display the intro:
print('''Birthday Paradox, by Al Sweighart

The Birthday Paradox shows is that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.
''')

#Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) >=100):
        numBDays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(numBDays):
    if i != 0:
        # Display a comma for each birtday after the first birtday.
        print(',', end='')
