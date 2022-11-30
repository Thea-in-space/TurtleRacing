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

MILESTONE 3
Goal: 
Begin to implement a point/money system. Start with $50. Use “command” to get the user to bet an amount of money. Check against the point total (you can’t bet more than you have). Use “command” to get the user to guess which turtle will win. At the end of the race, check the guess against the winner, and if they match, add the bet to the point total. If they don’t match, subtract the guess. Check the point total against 0. If the point total is less than or equal to zero, game over.

Functions:
check_winner(guess)
check_points(current_total)
eval_points
get_bet
get_guess
Variables:
user_guess
user_bet
current_points

MILESTONE 4
Goal:
Write and update the point counter on screen. CHALLENGE: Display the expressions (add or subtract) next to the point count as the point count updates.

Variables:
pointturtle
updateturtle

MILESTONE 5
Goal:
Random disqualifications. 
Racers have a low chance of being disqualified from the race. If they are disqualified, regardless of speed, they cannot be the winner.


Functions:
race_go() 
find_winner()
rand_disqual()
Variables:
disqual_chance

MILESTONE 6
Goal:
Use global variables to access turtle names etc for disqualification and finding the winner and incorporating into all functions that use the names etc….

Functions:
all?

MILESTONE 7
Goal:
Make it prettier, do stylistic changes. 
Finish line
Display “game over” (clear screen? Display in middle)
Starting line
Race track (lanes)

MILESTONE 8
Goal: 
Do a new project that is the same but uses steps to make the turtles go at the same time.
