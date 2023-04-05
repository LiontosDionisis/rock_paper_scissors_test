from random import shuffle
rps = ["rock","paper","scissors"]
guess =""

wins = []
losses = []
game = True



def check_restart():
        check = input("Keep playing? y or n: ")
        global wins 
        global losses
        if check.lower() == "n":
            print("Bye Bye")
            wins.clear()
            losses.clear()
             
        else:
            pass
        
    
        
    

def game_on():
    while game is not False:
        shuffle(rps) 
        guess = input("Choose : rock , paper , scissors: ")
        if rps[0]=="rock":
            if guess.lower() =="rock":
                print("Tie")
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="rock":
            if guess.lower() =="paper":
                print("You've won!")
                wins.append(1)
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="rock":
            if guess.lower() =="scissors":
                print("You've lost")
                losses.append(1)
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()                
        if rps[0]=="paper":
            if guess.lower() =="paper":
                print("Tie")
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="paper":
            if guess.lower() =="rock":
                print("You've lost")
                losses.append(1)
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="paper":
            if guess.lower() =="scissors":
                print("You've won")
                wins.append(1)
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="scissors":
            if guess.lower() =="rock":
                print("You've won")
                wins.append(1)
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="scissors":
            if guess.lower() =="paper":
                print("You've lost")
                losses.append(1)
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
        if rps[0]=="scissors":
            if guess.lower() =="scissors":
                print("Tie")
                print(f"wins : {len(wins)}")
                print(f"losses : {len(losses)}")
                check_restart()
            
game_on()
                
            
