from random_word import RandomWords

def hagmanpic(pic):  #returns ascii graphic of hangman by number of wrong guesses
  HANGMANPICS = [    '''
  +---+
      |
      |
      |
      |
      |
=========''', 
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
  return HANGMANPICS[pic]

def wordgen(): #returns random word
    word = RandomWords()
    
    word=word.get_random_word()
    
    return (word)

def hideword(word,guesses): #generates string with the guessed letters and the remaining ones in form of "_"
    word=word.replace("-", "") #removes "-" character from randomnly generated string
    
    word=word.replace("'", "") #removes "'" character from randomnly generated string
    
    hiddenword="_ "*len(word) #generates a string a hidden version of random word in form of "_ _ _ _ _"

    hiddenword=hiddenword.split()

    guesses=guesses.split(sep=",") 



    for letters in range(0, len(word)): #checks if the guessed letter its in word if its there unihides from hidden version of word the parts of that letter
        
        for character in guesses:
          
          if character==word[letters]:
            
            hiddenword[letters]=character

    if "_" not in hiddenword: #checks if the word is completed 
      
      print ("Congratulations you managed to find the word by letter to letter guessing")
    
    hiddenword= ' '.join([str(elem) for elem in hiddenword]) #converts hiddenword to string
    
    return hiddenword #returns hidden version of word or the guessed parts of it


def mainmenu():
    
    wrongguesses=0 #stores the number of wrong guesses
    
    word=wordgen() #stores the random word from word generator function
    
    word=word.upper()
    
    
    letter="" #stores single guess
    
    guesses=""#stores every guess user typed
  
    print (""" .----------------.  .----------------.  .-----------------. .----------------.   .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | | | | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | | | ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | | | |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | | | |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | | | | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | | | ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | | | |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------' 
 """)

    
    while True: #main loop
        
        print (hideword(word,guesses) +"""\t\t\t\t\t\t\t\t\t\n """+hagmanpic(wrongguesses) + "\t\n")

        
        letter=input("Guess a letter or the word: ")

        letter=letter.upper()
        
        guesses+=letter+","
        

        
        
        if letter in word:
            print ("\t \t you guessed right \n")


        else:
            print ("\t \t wrong guess \n")

            wrongguesses+=1


        if wrongguesses == 7:
          
          print ("""\t\t\t\t"""+hagmanpic(wrongguesses)+"\n")

          print ("you didn't manage to save him, he got hanged to death")
          
          break
        
        if letter==word:
          
          print ("Congratulations! you found the word")
          
          break

mainmenu()