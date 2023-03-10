"""Bouncing DVD Logo, by Al Sweigart
A bouncing DVD logo animation. You have to be 'of a certain age' to
appreciate this. Press Ctrl-C to stop.

NOTE:  Do not resize the terminal window while this program is running.
View this code at http://nostarch.com/big-book-small-python-projects
Tags: short, artistic, bext"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width be one:
WIDTH -= 1

number_of_logos = 5  # (!) Try changing this to 1 or 100
pause_amount = 0.2  # (!) Try changing this to 1.0 or 0.0.
# Try changing this list to fewer colors:
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

up_right = 'ur'
up_left = 'ul'
down_right = 'dr'
down_left = 'dl'
directions = (up_right, up_left, down_right, down_left)

# Key names for logo dictionaries:
color = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # Generate some logs.
    logos = []
    for i in range(number_of_logos):
        logos.append({color: random.choice(colors),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(directions)})
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner.
            logos[-1][X] -= 1

    corner_bounces = 0  # Count how many times a logo hits a corner.
    while True:  # Main program loop.
        for logo in logos:  # Handle each logo in the logos list.
            # Erase the logo's current location:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')  # (!) Try comment ing this line out.

            original_direction = logo[DIR]

            # See if the logo bounces off the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = down_right
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = up_right
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = down_left
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = up_left
                corner_bounces += 1

            # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == up_left:
                logo[DIR] = up_right
            elif logo[X] == 0 and logo[DIR] == down_left:
                logo[DIR] = down_right

            # See if the logo bounces off the right edge:
            # (WIDTH - 3 because 'DVD' has 3 letters.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == up_right:
                logo[DIR] = up_left
            elif logo[X] == WIDTH - 3 and logo[DIR] == down_right:
                logo[DIR] = down_left

            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == up_left:
                logo[DIR] = down_left
            elif logo[Y] == 0 and logo[DIR] == up_right:
                logo[DIR] = down_right

            # See if the logo bounces off the bottom edge:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == down_left:
                logo[DIR] = up_left
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == down_right:
                logo[DIR] = up_right

            if logo[DIR] != original_direction:
                # Change color when the logo bounces:
                logo[color] = random.choice(colors)

            # Move the logo. (X moves by 2 because the terminal
            # characters are twice as tall as they are wide.)
            if logo[DIR] == up_right:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == up_left:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == down_right:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == down_left:
                logo[X] -= 2
                logo[Y] += 1

        # Display number of corner bounces:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', corner_bounces, end='')

        for logo in logos:
            # Draw the logos at their new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[color])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(pause_amount)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()  # When Ctrl-C is pressed, end the program.
