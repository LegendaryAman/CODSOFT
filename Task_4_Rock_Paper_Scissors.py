import random
def Rock_paper_Scissors():
    print("________________________________INSTRUCTIONS_______________________________________\n")
    print("1. To Play Rock Paper Scissors Game select the number of round you want to play \n2. player with maximum round will wil the Game \n\n ********************ALL THE BEST ********************")
    print("\n Enter Numbrer of Round You Want to Play")
    round = int(input())
    R,P,S = 1,2,3
    p,c = 0,0
    r = 1
    while r <= round:
            r += 1
            computer = random.choice([R,P,S])
            print("\nPress R for Rock P for Paper and S for Scissor")
            user_value = input().upper()
            if(user_value == 'R' and computer ==  R):
                print("Tie")
            elif(user_value == 'R' and computer == P):
                print("Loose")
                c += 1
            elif(user_value == 'R' and computer == S):
                print("Win")
                p += 1
            elif(user_value == 'P' and computer == R):
                print("Win")
                p += 1
            elif(user_value == 'P' and computer == P):
                print("Tie")
            elif(user_value == 'P' and computer == S):
                print("Loose")
                c += 1
            elif(user_value == 'S' and computer == R):
                print("Loose")
                c += 1
            elif(user_value == 'S' and computer == P):
                print("Win")
                p += 1
            elif(user_value == 'S' and computer == S):
                print("Tie")
            else:
                print("Enter a valid input ")
                r -= 1
    print()
    if(p > c):
        print(f"Your Score : {p}\t Computer Score : {c}\nCongrutulation!!! YOU WON")    
    elif(c > p):
        print(f"Your Score : {p}\t Computer Score : {c}\nYOU LOOSE")
    else:
        print(f"Your Score : {p}\t Computer Score : {c}\nTIE")
Rock_paper_Scissors()