import sys
sys.stdin.flush()

x = "Hello"[0]
print (x)

name = input("Enter your name: ")
print(f"Hello, {name}!")

print("DEBUG: Waiting for user input...")
sys.stdin.flush()
player_input = input("Do you want to draw another card? (Y/N): ").strip().lower()
print(f"DEBUG: You entered {player_input}")