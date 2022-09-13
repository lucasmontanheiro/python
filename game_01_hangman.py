# Game Hangman

word = "house"
chances = 0
display = ""
guesses = []
display2 = len(word)*"_ "

def hangmanWord(guess):
  if word.find(guess):
    display2.replace("_", guess)
  return display2

while chances <= (len(word) - 1):
  
  name1 = input("Enter letter: ")

  print("Your guess: " + name1)

  guesses.append(name1)

  for w in word:
    if w == name1:
      hangmanWord(name1)
  chances += 1

  print(display2)
  print(f'You have {len(word) - chances} chances!')