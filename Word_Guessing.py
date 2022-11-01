import random

words = {
    'fruits': ['mango', 'banana', 'apple', 'orange', 'grapes'],
    'sports': ['basketball', 'football', 'handball', 'cricket', 'kho-kho'],
    'continents': ['asia', 'antartica', 'africa', 'north america', 'south america', 'europe'],
    ' sports players':['ronaldo', 'messi', 'virat', 'sachin', 'dhoni'],
    'country': ['india', 'USA', 'russia', 'china', 'brazil'],
}
a = random.choice(list(words.items()))
hint = a[0]

random_word = random.choice(a[1])
print("Your hint for the word is: ", hint)

run = True
user_input = []

while run:
    gameOver = True
    for i in random_word:
        if i in user_input:
            print(i, end=" ")
            gameOver = True
        else:
          print("_", end=" ")
          gameOver = False 
    if gameOver == True:
        print("You won the game")
        break
      
          
    k = input('Enter a letter: ')
    user_input.append(k)
    if k not in random_word:
      print('wrong input')
    