def start():
  print("Welcome to the game! You are standing at the lakeshore on Promontory Point. Do you swim (s) or walk around (w)")
  choice = input()
  if choice=="s":
    swim()
  elif choice=="w":
    walk()
  else:
    start()

def swim():
  print("You jump into the lake and start swimming around. The Loch Ness monster eats you. You lose. Try again? (y/n)")
  choice = input()
  if choice == "y":
    start()
  if choice == "n":
    end()
  else:
    swim()

def walk():
  print("You walk along the lakeshore. While you cross the bike path, a giant tricycle runs you over. You lose.")
  choice = input()
  if choice == "y":
    start()
  if choice == "n":
    end()
  else:
    walk()

def end():
  print("The end.")
  quit()


start()
