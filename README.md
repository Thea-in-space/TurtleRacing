# TurtleRacing
Bet on turtle racing.

MILESTONE 1
Goal: Get 4 Turtles up and running, going the same distance at randomized speeds every time the program runs.

Functions:
randomize_speed
race_go
Variables:
Turtles 1-4 (names TBD)
Every turtle has a speed (turtle.speed()) randomized each turn
Every turtle has a color, starts on turtle setup and remains constant
race_distance (same every time, maybe a global variable?)


MILESTONE 2
Goal:  Put the race_go function into a while loop that resets the turtles to their original position after each race and randomizes a new speed. At the end of each race, evaluate the winner (fastest/greatest speed), save it, and print it. For now, just add a user input at the beginning of each loop that breaks the loop if the input is “Quit” but lets it go for anything else.

Functions and program elements affected:  List program elements that might be affected by this goal.

Functions: 
race_go (now inside a loop)
race_reset
set_heading and set_pos (maybe just set_pos since the turtles won’t be turning. This is a straight line race.)
Variables:
heading and pos for each turtle, probably saved as name_heading and name_pos (unless we can get a function to do this without saving and individual variable for each turtle)
race_winner 
user_command (only checks for quit, anything else just goes)


