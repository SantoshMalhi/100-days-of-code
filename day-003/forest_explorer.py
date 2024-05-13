import time

# Function for introducing the game
def introduction():
    print("Welcome to Forest Explorer!")
    time.sleep(1)
    print("You find yourself at the edge of the Enchanted Forest.")
    time.sleep(1)
    print("Your quest is to uncover the secrets hidden within.")
    time.sleep(1)

# Function for exploring the forest
def explore_forest():
    print("\nYou venture deeper into the forest...")
    time.sleep(2)
    print("You encounter a fork in the path.")
    choice = input("Do you go left or right? (left/right): ").lower()
    if choice == "left":
        print("You discover a hidden glade with shimmering fireflies.")
        time.sleep(2)
        print("You collect a jar of fireflies.")
        inventory.append("fireflies")
    elif choice == "right":
        print("You stumble upon an ancient ruin covered in vines.")
        time.sleep(2)
        print("You find a mystical artifact.")
        inventory.append("mystical artifact")
    else:
        print("Invalid choice. Please try again.")
        explore_forest()

# Function for displaying inventory
def show_inventory():
    print("\nInventory:")
    for item in inventory:
        print("-", item)

# Main function to run the game
def main():
    introduction()
    while True:
        explore_forest()
        show_inventory()
        choice = input("\nDo you want to continue exploring? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for playing Forest Explorer!")
            break

# Initialize inventory
inventory = []

# Run the game
main()
