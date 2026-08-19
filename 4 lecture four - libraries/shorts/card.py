import random


cards = ["jack", "queen", "king"]



def main():
    # choose one from list 
    # print(random.choice(cards)) 



    '''
    random.choices() chooses 2 instead of just 1 item from list 
    random.choices() does sampling with replacement
    ie choosing a card, making a note of it, then placing it back in the deck 
    so it can be chosen again.
    this could result in two of the same items being chosen
    '''
    # print(random.choices(cards, k=2)) 



    # random.sample() does sampling without replacement;
    # ie it chooses two distinct items 
    # print(random.sample(cards, k=2))


    # the weights parameter makes it more likely on a scale of 0 to 100 
    # that an index will be called 
    # print(random.choices(cards, weights=[100, 0, 0], k=2))
    # print(random.choices(cards, weights=[75, 20, 5], k=2))


    # you want to think of debugging as defined inputs and defined outputs
    # debugging with the random module using the seed function:
    # research what exactly is the seed
    # random.seed() with an argument forces the generator to start at the exact same point. 
    # running the program multiple times will yield identical results, 
    # which is essential for debugging, testing, and machine learning.
    # numeric argument in random.seed(x) acts as a permanent starting position for Python's random number generator.
    random.seed(0)
    print(random.choices(cards, k=2)) 



main()


