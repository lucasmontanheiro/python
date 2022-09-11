# Game Hangman

word = "house"
chances = 0
display = ""

while chances <= (len(word) - 1):
  
  name1 = input("Enter letter: ")

  print("Your guess: " + name1)

  for w in word:
    if w == name1:
      display += " " + name1
    else:
      display += " _"
  chances += 1

  print(display)
  print(f'You have {len(word) - chances} chances!')