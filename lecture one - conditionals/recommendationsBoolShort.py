# from shorts, not lecture 
# BOOLEAN EXPRESSIONS
# boolean expresions has a yes or no response, true or false
# 3 boolean operators: OR NOT AND



def main():
    difficulty = input("Difficult or Casual? ")
    if difficulty == "Difficult" or difficulty == "Casual":



    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else: 
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else: 
            print("Enter a valid number of players")
    else: 
        print("Enter a valid difficulty")



def recommend(game):
    print("You might like", game)



main()