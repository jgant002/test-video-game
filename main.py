username = "IamMe"
password = "ThisisMe"
computer_open = "False"
attempts = 0


player_username = input(print("Type your username:"))
print(player_username)

player_password = input(print("Type your password:"))
print(player_password)

while computer_open == "False":
  if player_username == username and player_password == password:
    print(f"(✅) Welcome {username}!")
    computer_open = "True"
    
  elif player_username != username: 
    player_username = input(print("(❌) Incorrect, type your username again:"))
    attempts += 1
    if attempts == 3:
      print("You have been locked out")
      computer_open = "Locked"
  elif player_password != password:
    player_password = input(print("(❌) Incorrect, type your password again:"))
    attempts += 1
    if attempts == 3:
      print("You have been locked out")
      computer_open = "Locked"
while computer_open == "Locked":
  puzzle_15th = input(print("(🔒) Enter the 15th letter of the alphabet:"))
  if puzzle_15th == "O" or puzzle_15th == "o":
    computer_open = False
  else: 
    computer_open = "Soft Locked"
    print("(☠️) Error: too many incorrect attempts, you have been locked out of the \
software.")

