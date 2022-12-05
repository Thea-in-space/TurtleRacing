import turtle, random, time
   

#window setup
wn = turtle.Screen()
wn.bgcolor('lightcyan')

#racetrack setup
#starting line
trackturt = turtle.Turtle()
trackturt.penup()
trackturt.hideturtle()
trackturt.setpos(-190, 125)
trackturt.right(90)
trackturt.pendown()
trackturt.forward(200)
trackturt.penup()
#finish line
trackturt.setpos(210, 125)
trackturt.pendown()
trackturt.forward(200)
trackturt.penup()
trackturt.left(90)
#lanes
y = 125
x = -190
for i in range(1,6):
  trackturt.setpos(x, y)
  trackturt.pendown()
  trackturt.forward(400)
  trackturt.penup()
  y = y - 50

#start and finish text
#use trackturt, he does a good job

c = turtle.getcanvas()
item_id = c.create_text(-270, -10, text = "START", angle = 90, font = ("Arial Rounded MT Bold", 20))

d = turtle.getcanvas()
item_id2 = d.create_text(250, -10, text = "FINISH", angle = -90, font = ("Arial Rounded MT Bold", 20))
#racer initialization
inky = turtle.Turtle()
inky.shape("turtle")
inky.color("cyan")
inky.penup()
inky.setpos(-200, 100)
ipos = inky.pos()

blinky = turtle.Turtle()
blinky.shape("turtle")
blinky.color("red")
blinky.penup()
blinky.setpos(-200, 50)
bpos = blinky.pos()


pinky = turtle.Turtle()
pinky.shape("turtle")
pinky.color("pink")
pinky.penup()
pinky.setpos(-200, 0)
ppos = pinky.pos()

clyde = turtle.Turtle()
clyde.shape("turtle")
clyde.color("orange")
clyde.penup()
clyde.setpos(-200, -50)
cpos = clyde.pos()

#Ready...set...GO
def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key
 
    return "key doesn't exist"




def randomize_speed(turtles):
  for racer in turtles:
    racer.speed(random.randint(1,9))


def check_winner(winner, guess):
  if guess == winner:
    #add points
    right = True
    print("You guessed correctly!")
  elif guess == None:
    #do nothing
    right = None
    print("You didn't guess, or you submitted an invalid guess")
  else:
    right = False
    print("You guessed wrong. :( ")
    
  return right

def race_go(): 
  randomize_speed(turtles)
  fastest = 0
  speeds = {}
  disqualed = rand_disqual(turtles)
  for racer in turtles:
    index = turtles.index(racer)
    if racer in disqualed:
      dis = random.randint(50,350)
      racer.forward(dis)
      time.sleep(1)
    else:
      racer.forward(DISTANCE)
      time.sleep(1)
      speeds[names[index]] = racer.speed()
  
  for num in speeds.values():
    if num >= fastest:
      fastest = num
  winner = get_key(fastest, speeds)
  return winner
      

def reset(t1, t2, t3, t4):
  inky.setpos(ipos)
  blinky.setpos(bpos)
  pinky.setpos(ppos)
  clyde.setpos(cpos)


def get_bet():
  user_bet = input("How many buttons would you like to bet that you're right? Answer an integer. ")
  try:
    true_bet = int(user_bet)
  except ValueError:
    print("Bet an integer next time. Your bet has been set to 0.")
    true_bet = 0
  if true_bet > points:
    print("You can't bet more than you have. Your bet has been set to 0.")
    true_bet = 0
  return true_bet

def get_guess():
  valid_guesses = ["Inky", "inky", "Pinky", "pinky", "Blinky", "blinky", "Clyde", "clyde"]
  user_guess = input("Which racer do you think went the fastest?: Inky, Blinky, Pinky, or Clyde? ")
  if user_guess not in valid_guesses:
    print("Guess a valid racer next time.")
    user_guess = None
  return user_guess
  
def rand_disqual(turtles):
  disqual_racers = []
  for racer in turtles:
    index = turtles.index(racer)
    turtle_rand = random.randint(1,100)
    if turtle_rand < 5:
      disqual_racers.append(racer)
      print(f"{names[index]} was disqualified!")
  return disqual_racers

  
#main program


#meown program
DISTANCE = 400
turtles = [inky, blinky, pinky, clyde]
names = ["inky", "blinky", "pinky", "clyde"]
command = None
points = 100
num_races = 0

print("You have 100 buttons to start with. Guess which racer will win! If the racers tie, the one that went first is the winner. Top down: Inky, Blinky, Pinky, Clyde. Be careful: the game will end if you hit 0 buttons.")

pointturtle = turtle.Turtle()
pointturtle.color('black')
updateturtle = turtle.Turtle()
pointturtle.hideturtle()
updateturtle.hideturtle()

goturt = turtle.Turtle()

while command != "quit":

  pointturtle.penup()
  updateturtle.penup()
  pointturtle.setpos(-200, -100)
  pointturtle.pendown()
  pointturtle.write(f"Buttons: {points}", font = ("Arial Rounded MT Bold", 12))
  
  time.sleep(2)
  goturt.penup()
  goturt.hideturtle()
  goturt.setpos(-50, -100)
  goturt.color("red")
  goturt.write("READY", font = ("Arial Rounded MT Bold", 12))

  
  time.sleep(1)

  goturt.setpos(20, -100)
  goturt.color("yellow")
  goturt.write("SET", font = ("Arial Rounded MT Bold", 12))

  
  time.sleep(1)

  goturt.setpos(70, -100)
  goturt.color("green")
  goturt.write("GO!", font = ("Arial Rounded MT Bold", 12))

  time.sleep(1)
  goturt.clear()
  

  updateturtle.setpos(-100, -100)

 
  num_races = num_races + 1
  
  
  
  winner = race_go()
  user_guess = get_guess()
  user_bet = get_bet() 
  print(f'The winner is {winner}')
  print(f"  inky: {inky.speed()}")
  print(f"  blinky: {blinky.speed()}")
  print(f"  pinky: {pinky.speed()}")
  print(f"  clyde: {clyde.speed()}")
  
  check = check_winner(winner, user_guess)
  if check == True:
      points = points + user_bet
      updateturtle.clear()
      updateturtle.color('green')
      updateturtle.pendown()
      updateturtle.write(f'+{user_bet}', font = ("Arial Rounded MT Bold", 12))
      
  elif check == False:
      points = points - user_bet
      updateturtle.clear()
      updateturtle.color('red')
      updateturtle.pendown()
      updateturtle.write(f'-{user_bet}', font = ("Arial Rounded MT Bold", 12))
  elif check == None:
      updateturtle.clear()
      points = points
  print(f'You now have {points} buttons!')
  if points <= 0:
    wn.clear()
    wn.bgcolor('lightcyan')
    pointturtle.setpos(-200,-50)
    pointturtle.color("red")
    pointturtle.write("GAME OVER", font = ("Arial Rounded MT Bold", 50))
    print("GAME OVER!")
    break
  
  pointturtle.clear()
  pointturtle.write(f"Buttons: {points}", font = ("Arial Rounded MT Bold", 12))

  reset(inky, blinky, pinky, clyde)

  command = input("Press enter to continue. Enter 'quit' if finished: ")
