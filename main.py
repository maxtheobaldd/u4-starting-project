"""
Games Club Statistics Program - Unit 4: Starting Project
A simple program to record player scores and calculate statistics and write them to a txt file
https://github.com/maxtheobaldd/u4-starting-projectfg
"""

def main():
    """
    Main function that runs the whole program
    Shows a menu and keeps running until user wants to exit
    """
    print("Welcome to Games Club Statistics Program")
    print("=" * 50)
    
    # Keep showing the menu until user chooses to exit
    while True:
        choice = show_menu()
        
        if choice == "1":
            record_scores()
        elif choice == "2":
            show_saved_stats()
        elif choice == "3":
            print("\nThanks for using the Games Club Program!")
            print("Goodbye!")
            break
        else:
            print("That's not a valid choice. Please pick 1, 2, or 3.")
            input("Press Enter to try again...")

def show_menu():
    """
    Shows the main menu and gets the user's choice
    Returns what the user picked as a string
    """
    print("\n" + "=" * 50)
    print("GAMES CLUB STATISTICS PROGRAM")
    print("=" * 50)
    print("1. Record Player Scores")
    print("2. Show Saved Player Stats")
    print("3. Exit Program")
    print("=" * 50)
    
    choice = input("What would you like to do? (1-3): ")
    return choice

def get_player_id():
    """
    Gets a valid player ID from the user
    Keeps asking until they enter something good
    """
    while True:
        player_id = input("Enter Player ID: ").strip()
        
        # Check if they entered nothing
        if len(player_id) == 0:
            print("Oops! You can't leave this empty. Try again.")
        # Check if it's too long
        elif len(player_id) > 20:
            print("That's too long! Keep it under 20 characters.")
        else:
            # Make it uppercase so it looks consistent
            return player_id.upper()

def get_number_of_games():
    """
    Gets how many games the player played and ensures its a positive number
    """
    while True:
        try:
            num_games = int(input("How many games did you play? "))
            
            if num_games <= 0:
                print("You need to have played at least 1 game!")
            elif num_games > 100:
                print("Wow, that's a lot! Let's keep it under 100 games.")
            else:
                return num_games
                
        except ValueError:
            print("Please enter a number, not letters!")

def get_score():
    """
    Gets a valid score from the user
    Must be a positive number (or zero)
    """
    while True:
        try:
            score = int(input("Enter your score: "))
            
            if score < 0:
                print("Scores can't be negative! Try again.")
            elif score > 1000000:
                print("That's an amazing score, but let's keep it under 1,000,000!")
            else:
                return score
                
        except ValueError:
            print("Please enter a number for the score!")

def get_time():
    """
    Gets a valid time from the user
    Must be a positive decimal number
    """
    while True:
        try:
            time = float(input("How long did you play (in minutes)? "))
            
            if time <= 0:
                print("Time must be more than 0 minutes!")
            elif time > 1440:  # 1440 minutes = 24 hours
                print("That's more than 24 hours! Are you sure?")
            else:
                return time
                
        except ValueError:
            print("Please enter a number for the time!")

def record_scores():
    """
    Main function to record all player data
    Gets player info, scores, times, then calculates and saves everything
    """
    print("\n" + "=" * 50)
    print("RECORD PLAYER SCORES")
    print("=" * 50)
    
    # Get basic player information
    player_id = get_player_id()
    num_games = get_number_of_games()
    
    # Create empty lists to store all the scores and times
    scores = []  # Will hold all scores like [1200, 1500, 1800]
    times = []   # Will hold all times like [25.0, 20.5, 30.0]
    
    # Get data for each game
    print(f"\nOkay! Let's enter data for {num_games} games:")
    print("-" * 30)
    
    # Loop through each game
    for game_number in range(1, num_games + 1):
        print(f"\nGame {game_number}:")
        
        # Get score and time for this game
        score = get_score()
        time = get_time()
        
        # Add them to our lists
        scores.append(score)
        times.append(time)
        
        print(f"  Got it! Score = {score}, Time = {time} minutes")
    
    # Calculate the statistics
    print("\nCalculating your stats...")
    highest_score = find_highest_score(scores)
    average_time = calculate_average_time(times)
    
    # Show the results
    show_results(player_id, scores, times, highest_score, average_time)
    
    # Save to file
    save_to_file(player_id, scores, times, highest_score, average_time)
    
    print("\n" + "=" * 50)
    print("All done! Your data has been saved!")
    print("=" * 50)
    input("Press Enter to go back to the main menu...")

def find_highest_score(scores):
    """
    Finds the highest score in a list of scores
    Takes a list like [1200, 1500, 1800] and returns 1800
    """
    if len(scores) == 0:  # Just in case the list is empty
        return 0
    
    # Use Python's built-in max() function to find the biggest number
    return max(scores)

def calculate_average_time(times):
    """
    Calculates the average time from a list of times
    Takes a list like [25.0, 20.5, 30.0] and returns 25.17
    """
    if len(times) == 0:  # Just in case the list is empty
        return 0.0
    
    # Add up all the times
    total_time = sum(times)
    
    # Divide by how many times we have to get the average
    average = total_time / len(times)
    
    # Round to 2 decimal places so it looks nice
    return round(average, 2)

def show_results(player_id, scores, times, highest_score, average_time):
    """
    Shows all the player statistics in a nice format
    Makes everything look organized and easy to read
    """
    print("\n" + "=" * 60)
    print("YOUR GAME STATISTICS")
    print("=" * 60)
    
    # Show basic info
    print(f"Player ID: {player_id}")
    print(f"Number of games played: {len(scores)}")
    print(f"Highest Score: {highest_score:,}")  # :, adds commas to big numbers
    print(f"Average Time per Game: {average_time} minutes")
    
    print("\n" + "-" * 60)
    print("ALL YOUR GAME DATA")
    print("-" * 60)
    
    # Show all scores with game numbers
    print("All Your Scores:")
    for i in range(len(scores)):
        game_num = i + 1  # Add 1 because we want to start from Game 1, not Game 0
        print(f"  Game {game_num}: {scores[i]:,} points")
    
    # Show all times with game numbers
    print("\nAll Your Times:")
    for i in range(len(times)):
        game_num = i + 1
        print(f"  Game {game_num}: {times[i]} minutes")
    
    # Calculate and show total time
    total_time = sum(times)
    print(f"\nTotal Time Played: {total_time} minutes")
    
    print("=" * 60)

def save_to_file(player_id, scores, times, highest_score, average_time):
    """
    Saves all player data to a text file
    Creates a file named 'player_PLAYERID.txt'
    """
    # Create filename using the player ID
    filename = f"player_{player_id}.txt"
    
    try:
        # Open file for writing ('w' means write mode)
        # 'with' automatically closes the file when im done
        with open(filename, 'w') as file:
            
            # Write a nice header
            file.write("GAMES CLUB STATISTICS REPORT\n")
            file.write("=" * 40 + "\n")
            file.write(f"Report for Player: {player_id}\n")
            file.write("=" * 40 + "\n\n")
            
            # Write the main statistics
            file.write("SUMMARY:\n")
            file.write("-" * 20 + "\n")
            file.write(f"Player ID: {player_id}\n")
            file.write(f"Number of Games: {len(scores)}\n")
            file.write(f"Highest Score: {highest_score:,}\n")
            file.write(f"Average Time: {average_time} minutes\n")
            file.write(f"Total Time Played: {sum(times)} minutes\n\n")
            
            # write game data
            file.write("DETAILED GAME DATA:\n")
            file.write("-" * 20 + "\n")
            
            # write each games data
            for i in range(len(scores)):
                game_num = i + 1
                file.write(f"Game {game_num}: Score = {scores[i]:,}, Time = {times[i]} minutes\n")
            
            file.write("\n" + "=" * 40 + "\n")
            
            # write raw data (useful if someone wants to use it in another program)
            file.write("RAW DATA:\n")
            # Convert all numbers to text and join them with commas
            scores_text = ', '.join([str(score) for score in scores])
            times_text = ', '.join([str(time) for time in times])
            file.write(f"Scores: {scores_text}\n")
            file.write(f"Times: {times_text}\n")
            
        print(f"\nYour data has been saved to: {filename}")
        
    except Exception as e:
        # file write error handling
        print(f"Oops! Couldn't save the file: {e}")
        print("Your data couldn't be saved, but everything else worked fine.")

def show_saved_stats():
    """
    Shows previously saved player statistics
    Reads data from a file and displays it
    """
    print("\n" + "=" * 50)
    print("SHOW SAVED PLAYER STATS")
    print("=" * 50)
    
    # Get the player ID to look up
    player_id = get_player_id()
    filename = f"player_{player_id}.txt"
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:  # 'r' means read mode
            content = file.read()  # Read the entire file
            print("\n" + content)  # Show everything in the file
            
    except FileNotFoundError:
        # handling target file not existing
        print(f"\nSorry, no data found for player {player_id}")
        print("Make sure you've recorded scores for this player first!")
        
    except Exception as e:
        # catching any other file problems
        print(f"Oops! There was a problem reading the file: {e}")
    
    input("\nPress Enter to go back to the main menu...")

# This line runs the program when you execute this file
if __name__ == "__main__":
    main()