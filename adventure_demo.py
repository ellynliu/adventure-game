def hillel_lawn():
  print("You arrive at the front lawn of Hillel. Do you go inside(i) or go home(h)?")
  choice = input()
  if choice=="i":
    breakfast()
  elif choice=="h":
    home()
  else:
    hillel_lawn()

def home():
  print("You have a really boring day at home. You come back to Hillel the next day.")
  hillel_lawn()

def breakfast():
  print("You are greeted with breakfast. Do you choose a plain bagel(b) or a chocolate chip muffin(m)?")
  choice = input()
  if choice=="b":
    print("You take a bite of the bagel and are transported to another dimension!")
    other_dimension()
  elif choice=="m":
    ben_wants_muffin()
  else:
    breakfast()

def other_dimension():
  print("There are swirling colors floating around. A smiling turtle says hello. You see the universe as it really is, comprehending its very core. There is a hallway (h) and a door (d). Which do you pick?")
  choice = input()
  if choice=="d":
    print("That's interesting, the door led you right back to Hillel. Mr. Ben waves. You smile and wave back. Mr. Ben tells you to go to class.")
    go_to_class()
  else:
    print("The hallway continues infinitely.")
    other_dimension()


def ben_wants_muffin():
  print("Our wonderful manager of operations, Mr. Ben, also wants a chocolate chip muffin. There is only one left. Do you give him the muffin (g), fight him for it (f), or try to persuade him to take a bagel instead (b)?")
  choice=input()
  if choice=="g":
    ben_gives_key()
  elif choice=="f":
    ben_attack()
  elif choice=="b":
    print("He takes a second to think about it, then accepts. You take the muffin. Mr. Ben tells you to go to class.")
    go_to_class()
  else:
    ben_wants_muffin()

def ben_attack():
  print("Ben reaches into his very stylish cowboy boots and pulls out a pair of nunchucks (those aren't allowed on school property??!!) and he advances on you menacingly and starts to make a swing. Do you duck (d), run (r), or block (b)")
  choice = input()
  if choice=="d":
    duck()
  elif choice=="r":
    home()
  elif choice=="b":
    print("Your block is ineffective. You go home, defeated.")
    home()
  else:
    ben_attack()

def duck():
  print("You duck, he misses. You have a split second to make your next decision: grab his weapon (w), tackle him (t), or use the force (f)")
  choice = input()
  if choice=="f":
    use_the_force() 
  elif choice=="t":
    tackle()
  elif choice=="w":
    grab_weapon()
  else:
    duck()

def use_the_force():
  print("You can't use the force. You go home, defeated.")
  home()

def tackle():
  print("He is immovable! You go home, defeated.")
  home()

def grab_weapon():
  print("You successfully take his weapon! Mr. Ben flees, dropping a key on the ground. Do you take the key (k) or go to class (c)?")
  choice=input()
  if choice=="k":
    key_decision()
  elif choice=="c":
    go_to_class()
  else:
    grab_weapon()

def ben_gives_key():
  print("Mr. Ben gives you a key out of gratitude.")
  key_decision()

def key_decision():
  print("You have the key. You notice a glowing golden chest that you never noticed before. Do you use the key (k) or go to class (c)?")
  choice = input()
  if choice=="k":
    find_treasure()
  elif choice=="c":
    go_to_class()
  else:
    key_decisions()

def find_treasure():
  print("You put the key into the chest's lock and turn it very dramatically. You open it, and you find........the Gloves of Flawless Programming! When you wear them, you never have errors when you're coding!")
  print("Do you go home to try to sell them on Ebay for a fortune (f) or use them in class (c)?")
  choice = input()
  if choice=="c":
    go_to_class()
  elif choice=="f":
    mr_shaw()
  else:
    find_treasure()

def mr_shaw():
  print("As you think you've made your escape, Mr. Shaw catches you trying to leave. He gives you a very stern look and tells you to go to class.")
  go_to_class()

def go_to_class():
  print("You go to class. You have a great class.")
  end()

def end():
  print("The end.")

hillel_lawn()