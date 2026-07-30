# from shorts, not lecture 
# BOOLEAN EXPRESSIONS
# boolean expresions has a yes or no response, true or false
# 3 boolean operators: OR, NOT, AND
# boolean operators can be used to simplify conditionals



def main():

    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else: # putting an else because there's only 4 possible options
        recommend("Clock")


def recommend(game):
    print("You might like", game)

main()