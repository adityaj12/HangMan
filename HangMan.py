word = "secret"
guesses = 15

letters = set()
for letter in word:
  letters.add(letter)

corr_letters = set()

while guesses > 0 and (len(letters) != len(corr_letters)):

  string = ""
  for letter in word:
    if letter in corr_letters:
      string += letter + " "
    else: 
      string += "_ "
  print(string)
    
  print('')
  guess_letter = input("Guess a letter! You have " + str(guesses) + " guesses remaining! ")
  guesses -= 1

  if guess_letter in letters:
    corr_letters.add(guess_letter)
    
  if len(letters) == len(corr_letters):
    print("")
    print("Winner!")