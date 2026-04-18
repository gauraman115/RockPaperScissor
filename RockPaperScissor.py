import random
def get_choice():
  user=input("enter you choice:")
  options=["rock","paper","scissor"]
  computer=random.choice(options)
  choices={"player_choice":user,"computer_choice":computer}
  return choices


def check_win(player,computer):
  print(f"you chose {player} and computer chose {computer}")

  if(player==computer):
     return("Its a tie!")
  
  elif(player=="rock"):
     if computer=="paper":
        return("paper covers rock, computer wins!")
     else:
        return("Rock crushes scissor, player wins!")
     
  elif(player=="paper"):
     if computer == "rock":
            return "Paper covers rock! You win!"
     else:
            return "Scissors cuts paper! You lose."
  
  elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
  
function=get_choice()
result=check_win(function["player_choice"],function["computer_choice"])
print(result)
  