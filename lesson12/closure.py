def parent_function(person):
    coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print(f"\n{person} has {coins} coins left!") 
        elif coins == 1:
            print(f"\n{person} has {coins} coins left!") 
        else:
            print(f"\n{person} is out of coins!") 
            
    return play_game

tommy = parent_function("tommy")
jenny = parent_function("jenny")
tommy()
tommy()
tommy()
jenny()


