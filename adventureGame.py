def play_game():
    # Start the game
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")
    first_option = input("Type 'MATCH' or 'FLASHLIGHT': ").strip().upper()

    if first_option == "MATCH":
        print("You pick up the match and light it, and for a moment, the forest around you is illuminated.")
        print("You see a large grizzly bear, and then the match burns out.")
        print("Do you want to RUN or HIDE behind a tree?")
        
        second_option = input("Type 'RUN' or 'HIDE': ").strip().upper()
        
        if second_option == "RUN":
            print("You run as fast as you can, but the bear catches you. Game Over!")
        elif second_option == "HIDE":
            print("You hide behind a tree. The bear walks away. Now you can either LEAVE or STAY STILL.")
            
            third_option = input("Type 'LEAVE' or 'STAY STILL': ").strip().upper()
            
            if third_option == "LEAVE":
                print("You slowly emerge and find your way back. You survived!")
            elif third_option == "STAY STILL":
                print("You remain still, and the bear ignores you. Eventually, it leaves. You survived!")
            else:
                print("Invalid option. Game over.")
        else:
            print("Invalid option. Game over.")

    elif first_option == "FLASHLIGHT":
        print("You pick up the flashlight and turn it on. You see the path illuminated in front of you.")
        print("But you think you also heard something to the side.")
        print("Do you want to FOLLOW the path or LOOK in the trees to see what made the noise?")
        
        second_option = input("Type 'FOLLOW' or 'LOOK': ").strip().upper()
        
        if second_option == "FOLLOW":
            print("You follow the path and arrive at a clearing with a lake. It's a beautiful spot!")
            print("Do you want to SWIM in the lake or REST on the shore?")
            
            third_option = input("Type 'SWIM' or 'REST': ").strip().upper()
            
            if third_option == "SWIM":
                print("You swim in the lake and enjoy a refreshing moment. You had a great adventure!")
            elif third_option == "REST":
                print("You rest on the shore and contemplate the beauty of the place. You had a great adventure!")
            else:
                print("Invalid option. Game over.")
        
        elif second_option == "LOOK":
            print("You look in the trees and see a small fox. The fox gets scared and runs away.")
            print("Now you can either FOLLOW the fox or GO BACK to the path.")
            
            third_option = input("Type 'FOLLOW' or 'GO BACK': ").strip().upper()
            
            if third_option == "FOLLOW":
                print("You follow the fox and discover a small den filled with treasures. You found a treasure!")
            elif third_option == "GO BACK":
                print("You return to the path and continue your adventure. You had a unique experience!")
            else:
                print("Invalid option. Game over.")
        
        else:
            print("Invalid option. Game over.")
    
    else:
        print("Invalid option. Game over.")

# Main loop to play the game
while True:
    play_game()
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
