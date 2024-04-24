from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)
score = 0
celeb_b = random.choice(data)
#Random generated celebs
#how to format account data into pritable format
game_continue = True
while game_continue:
  celeb_a = celeb_b
  celeb_b = random.choice(data)
  while celeb_a == celeb_b:
    celeb_b = random.choice(data)
    
  
  def format_data(celeb):
    """Takes the account data and returns the printable format."""
    celeb_name = celeb["name"]
    celeb_description = celeb["description"]
    celeb_country = celeb["country"]
    return f"{celeb_name}, a {celeb_description}, from {celeb_country}"
  
  def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
      return guess == "a"
    else:
      return guess == "b"
    
    
  print(f"Compare A: {format_data(celeb_a)}")
  
  print(vs)
  
  print(f"Against B: {format_data(celeb_b)}")
  
  guess = input(f"Who has more follower 'A' or 'B'").lower()
  
  a_follower_account = celeb_a["follower_count"]
  b_follower_account = celeb_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_account, b_follower_account)

  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're right, current score: {score}")
  else:
    game_continue = False
    print(f"You're wrong: Final score: {score}")
  
