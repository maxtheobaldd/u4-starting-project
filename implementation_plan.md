# Computer Games Club Statistics Program - Complete Implementation Guide

## Project Overview
This document provides the complete Python code for your Games Club Statistics Program, broken down into sections with detailed explanations. You can copy and paste these code sections to build your program step by step.

## Requirements Summary
- **Input**: Player ID, number of games, scores, and time for each game
- **Output**: Player ID, highest score, average time, and save data to file
- **Language**: Python 3.4+

---

## Section 1: Program Structure and Main Function

### What this section does:
This is the "brain" of your program. It controls everything and shows the main menu.

```python
def main():
    """
    Main program function - this controls the entire program
    It shows a menu and keeps running until the user chooses to exit
    """
    print("Welcome to Games Club Statistics Program")
    print("="*50)
    
    # This loop keeps the program running until user chooses to exit
    while True:
        choice = display_menu()  # Show menu and get user's choice
        
        if choice == "1":
            record_player_scores()  # Go to score recording
        elif choice == "2":
            display_statistics()    # Go to statistics display
        elif choice == "3":
            print("\nThank you for using Games Club Statistics Program!")
            print("Goodbye!")
            break  # This exits the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")  # Pause so user can read the error

def display_menu():
    """
    Shows the main menu options to the user
    Returns the user's choice as a string
    """
    print("\n" + "="*50)
    print("GAMES CLUB STATISTICS PROGRAM")
    print("="*50)
    print("1. Record Player Scores")
    print("2. Display Player Statistics")
    print("3. Exit Program")
    print("="*50)
    
    choice = input("Enter your choice (1-3): ")
    return choice

# This line runs your program when you execute the file
# It's like pressing the "start" button
if __name__ == "__main__":
    main()
```

### Key Points to Understand:
- `while True:` creates an infinite loop that keeps the menu showing
- `break` is the only way to exit the infinite loop
- `if __name__ == "__main__":` only runs when you execute this file directly

---

## Section 2: Input Validation Functions

### What this section does:
These functions make sure the user enters valid data. They keep asking until the user enters something correct.

```python
def get_valid_player_id():
    """
    Gets a valid player ID from the user
    Keeps asking until they enter something acceptable
    """
    while True:
        player_id = input("Enter Player ID: ").strip()  # .strip() removes extra spaces
        
        # Check if player ID is empty
        if len(player_id) == 0:
            print("Error: Player ID cannot be empty. Please try again.")
        # Check if player ID is too long
        elif len(player_id) > 20:
            print("Error: Player ID too long (maximum 20 characters). Please try again.")
        else:
            # If we get here, the player ID is valid
            return player_id.upper()  # Convert to uppercase for consistency

def get_valid_number_of_games():
    """
    Gets a valid number of games from the user
    Must be a positive integer
    """
    while True:
        try:
            # try/except handles the error if user enters non-numbers
            num_games = int(input("Enter number of games played: "))
            
            if num_games <= 0:
                print("Error: Number of games must be positive. Please try again.")
            elif num_games > 100:
                print("Error: Too many games (maximum 100). Please try again.")
            else:
                return num_games  # Valid number, return it
                
        except ValueError:
            # This runs if int() fails (user entered letters, etc.)
            print("Error: Please enter a valid number.")

def get_valid_score():
    """
    Gets a valid score from the user
    Must be a non-negative integer
    """
    while True:
        try:
            score = int(input("Enter score: "))
            
            if score < 0:
                print("Error: Score cannot be negative. Please try again.")
            elif score > 1000000:
                print("Error: Score too high (maximum 1,000,000). Please try again.")
            else:
                return score
                
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_time():
    """
    Gets a valid time from the user
    Must be a positive decimal number (float)
    """
    while True:
        try:
            time = float(input("Enter time in minutes: "))  # float() allows decimals
            
            if time <= 0:
                print("Error: Time must be positive. Please try again.")
            elif time > 1440:  # 1440 minutes = 24 hours
                print("Error: Time too long (maximum 24 hours). Please try again.")
            else:
                return time
                
        except ValueError:
            print("Error: Please enter a valid number.")
```

### Key Points to Understand:
- `try/except` catches errors when converting strings to numbers
- `int()` converts text to whole numbers, `float()` converts to decimal numbers
- `while True:` keeps asking until valid input is received
- `return` exits the function and gives back the valid value

---

## Section 3: Main Data Recording Function

### What this section does:
This is the main function that collects all the player data, calculates statistics, and saves everything.

```python
def record_player_scores():
    """
    Main function to record all player data
    This function coordinates everything: input, calculation, display, and saving
    """
    print("\n" + "="*50)
    print("RECORD PLAYER SCORES")
    print("="*50)
    
    # Step 1: Get basic player information
    player_id = get_valid_player_id()
    num_games = get_valid_number_of_games()
    
    # Step 2: Create empty lists to store this player's data
    scores = []  # Will store all scores: [1200, 1500, 1800]
    times = []   # Will store all times: [25.0, 20.5, 30.0]
    
    # Step 3: Get data for each game
    print(f"\nEntering data for {num_games} games:")
    print("-" * 30)
    
    # This loop runs once for each game
    for game_num in range(1, num_games + 1):  # range(1, 4) gives us 1, 2, 3
        print(f"\nGame {game_num}:")
        
        # Get score and time for this game
        score = get_valid_score()
        time = get_valid_time()
        
        # Add them to our lists
        scores.append(score)  # .append() adds to the end of a list
        times.append(time)
        
        print(f"  Recorded: Score = {score}, Time = {time} minutes")
    
    # Step 4: Calculate statistics
    print("\nCalculating statistics...")
    highest_score = calculate_highest_score(scores)
    average_time = calculate_average_time(times)
    
    # Step 5: Display results to user
    display_player_results(player_id, scores, times, highest_score, average_time)
    
    # Step 6: Save to file
    save_to_file(player_id, scores, times, highest_score, average_time)
    
    print("\n" + "="*50)
    print("Data recorded successfully!")
    print("="*50)
    input("Press Enter to return to main menu...")
```

### Key Points to Understand:
- `range(1, num_games + 1)` creates numbers from 1 to num_games
- Lists start empty `[]` and we use `.append()` to add items
- `f"text {variable}"` puts variables inside text strings
- The function calls other functions to do specific jobs

---

## Section 4: Calculation Functions

### What this section does:
These functions do the math to calculate the highest score and average time.

```python
def calculate_highest_score(scores):
    """
    Finds the highest score in a list of scores
    Takes a list like [1200, 1500, 1800] and returns 1800
    """
    if len(scores) == 0:  # Check if list is empty
        return 0
    
    # max() is a built-in Python function that finds the largest number
    return max(scores)

def calculate_average_time(times):
    """
    Calculates the average time from a list of times
    Takes a list like [25.0, 20.5, 30.0] and returns 25.17
    """
    if len(times) == 0:  # Check if list is empty
        return 0.0
    
    # sum() adds all numbers in the list
    total_time = sum(times)
    
    # Calculate average: total divided by count
    average = total_time / len(times)
    
    # round() limits to 2 decimal places: 25.166666 becomes 25.17
    return round(average, 2)

# Alternative manual calculation (more educational):
def calculate_average_time_manual(times):
    """
    Same as above but shows the math step by step
    This helps you understand what sum() does automatically
    """
    if len(times) == 0:
        return 0.0
    
    # Add up all the times manually
    total_time = 0
    for time in times:  # Go through each time in the list
        total_time = total_time + time  # Add it to our total
    
    # Calculate and return the average
    average = total_time / len(times)
    return round(average, 2)
```

### Key Points to Understand:
- `max()` and `sum()` are built-in Python functions
- `len()` tells you how many items are in a list
- Always check for empty lists to avoid errors
- `round(number, 2)` rounds to 2 decimal places

---

## Section 5: Display Results Function

### What this section does:
This function shows the results to the user in a nice, formatted way.

```python
def display_player_results(player_id, scores, times, highest_score, average_time):
    """
    Displays all the player statistics in a formatted way
    Makes the output look professional and easy to read
    """
    print("\n" + "="*60)
    print("PLAYER STATISTICS SUMMARY")
    print("="*60)
    
    # Basic information
    print(f"Player ID: {player_id}")
    print(f"Number of games played: {len(scores)}")
    print(f"Highest Score: {highest_score:,}")  # :, adds commas to big numbers
    print(f"Average Time per Game: {average_time} minutes")
    
    print("\n" + "-"*60)
    print("DETAILED GAME DATA")
    print("-"*60)
    
    # Show all scores with game numbers
    print("All Scores:")
    for i, score in enumerate(scores, 1):  # enumerate gives us position and value
        print(f"  Game {i}: {score:,} points")
    
    # Show all times with game numbers
    print("\nAll Times:")
    for i, time in enumerate(times, 1):
        print(f"  Game {i}: {time} minutes")
    
    # Calculate and show total time
    total_time = sum(times)
    print(f"\nTotal Time Played: {total_time} minutes")
    
    print("="*60)

def display_statistics():
    """
    Function to display previously saved player statistics
    Reads data from a file and shows it
    """
    print("\n" + "="*50)
    print("DISPLAY SAVED PLAYER STATISTICS")
    print("="*50)
    
    # Get the player ID to look up
    player_id = get_valid_player_id()
    filename = f"player_{player_id}.txt"  # Create filename
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:  # 'r' means read mode
            content = file.read()  # Read entire file
            print("\n" + content)  # Display the content
            
    except FileNotFoundError:
        # This error happens when the file doesn't exist
        print(f"\nNo data found for player {player_id}")
        print("Make sure you have recorded scores for this player first.")
        
    except Exception as e:
        # This catches any other file errors
        print(f"Error reading file: {e}")
    
    input("\nPress Enter to return to main menu...")
```

### Key Points to Understand:
- `f"text {variable}"` puts variables into text
- `{number:,}` formats numbers with commas (1,234 instead of 1234)
- `enumerate(list, 1)` gives you both position and value, starting from 1
- `try/except` handles file errors gracefully

---

## Section 6: File Handling Function

### What this section does:
This function saves all the player data to a text file so it's permanently stored.

```python
def save_to_file(player_id, scores, times, highest_score, average_time):
    """
    Saves all player data to a text file
    Creates a file named 'player_PLAYERID.txt'
    """
    # Create filename using player ID
    filename = f"player_{player_id}.txt"
    
    try:
        # Open file for writing ('w' means write mode)
        # 'with' automatically closes the file when done
        with open(filename, 'w') as file:
            
            # Write header
            file.write("GAMES CLUB STATISTICS REPORT\n")
            file.write("="*40 + "\n")
            file.write(f"Generated for Player: {player_id}\n")
            file.write("="*40 + "\n\n")
            
            # Write basic statistics
            file.write("SUMMARY STATISTICS:\n")
            file.write("-"*20 + "\n")
            file.write(f"Player ID: {player_id}\n")
            file.write(f"Number of Games: {len(scores)}\n")
            file.write(f"Highest Score: {highest_score:,}\n")
            file.write(f"Average Time: {average_time} minutes\n")
            file.write(f"Total Time Played: {sum(times)} minutes\n\n")
            
            # Write detailed game data
            file.write("DETAILED GAME DATA:\n")
            file.write("-"*20 + "\n")
            
            # Write each game's data
            for i in range(len(scores)):
                file.write(f"Game {i+1}: Score = {scores[i]:,}, Time = {times[i]} minutes\n")
            
            file.write("\n" + "="*40 + "\n")
            
            # Write raw data (useful for importing into other programs)
            file.write("RAW DATA:\n")
            file.write(f"Scores: {', '.join(map(str, scores))}\n")  # Convert numbers to text
            file.write(f"Times: {', '.join(map(str, times))}\n")
            
        print(f"\nData successfully saved to: {filename}")
        
    except Exception as e:
        # Handle any file writing errors
        print(f"Error saving file: {e}")
        print("Data could not be saved to file.")
```

### Key Points to Understand:
- `with open(filename, 'w')` safely opens a file for writing
- `file.write()` writes text to the file (doesn't automatically add new lines)
- `\n` creates a new line in the file
- `map(str, list)` converts all numbers in a list to text
- `', '.join(list)` combines list items with commas between them

---

## Section 7: Complete Program Code

### What this section does:
Here's the complete program with all sections combined. Copy this entire code into a file called `games_club_stats.py`:

```python
"""
Computer Games Club Statistics Program
Author: [Your Name]
Date: [Current Date]

This program records player scores and game times, then calculates and displays statistics.
It meets the requirements for the college computing course project.
"""

def main():
    """Main program function - controls the entire program"""
    print("Welcome to Games Club Statistics Program")
    print("="*50)
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            record_player_scores()
        elif choice == "2":
            display_statistics()
        elif choice == "3":
            print("\nThank you for using Games Club Statistics Program!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

def display_menu():
    """Shows the main menu options to the user"""
    print("\n" + "="*50)
    print("GAMES CLUB STATISTICS PROGRAM")
    print("="*50)
    print("1. Record Player Scores")
    print("2. Display Player Statistics")
    print("3. Exit Program")
    print("="*50)
    
    choice = input("Enter your choice (1-3): ")
    return choice

def get_valid_player_id():
    """Gets a valid player ID from the user"""
    while True:
        player_id = input("Enter Player ID: ").strip()
        
        if len(player_id) == 0:
            print("Error: Player ID cannot be empty. Please try again.")
        elif len(player_id) > 20:
            print("Error: Player ID too long (maximum 20 characters). Please try again.")
        else:
            return player_id.upper()

def get_valid_number_of_games():
    """Gets a valid number of games from the user"""
    while True:
        try:
            num_games = int(input("Enter number of games played: "))
            
            if num_games <= 0:
                print("Error: Number of games must be positive. Please try again.")
            elif num_games > 100:
                print("Error: Too many games (maximum 100). Please try again.")
            else:
                return num_games
                
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_score():
    """Gets a valid score from the user"""
    while True:
        try:
            score = int(input("Enter score: "))
            
            if score < 0:
                print("Error: Score cannot be negative. Please try again.")
            elif score > 1000000:
                print("Error: Score too high (maximum 1,000,000). Please try again.")
            else:
                return score
                
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_time():
    """Gets a valid time from the user"""
    while True:
        try:
            time = float(input("Enter time in minutes: "))
            
            if time <= 0:
                print("Error: Time must be positive. Please try again.")
            elif time > 1440:
                print("Error: Time too long (maximum 24 hours). Please try again.")
            else:
                return time
                
        except ValueError:
            print("Error: Please enter a valid number.")

def record_player_scores():
    """Main function to record all player data"""
    print("\n" + "="*50)
    print("RECORD PLAYER SCORES")
    print("="*50)
    
    # Get basic player information
    player_id = get_valid_player_id()
    num_games = get_valid_number_of_games()
    
    # Create empty lists to store data
    scores = []
    times = []
    
    # Get data for each game
    print(f"\nEntering data for {num_games} games:")
    print("-" * 30)
    
    for game_num in range(1, num_games + 1):
        print(f"\nGame {game_num}:")
        
        score = get_valid_score()
        time = get_valid_time()
        
        scores.append(score)
        times.append(time)
        
        print(f"  Recorded: Score = {score}, Time = {time} minutes")
    
    # Calculate statistics
    print("\nCalculating statistics...")
    highest_score = calculate_highest_score(scores)
    average_time = calculate_average_time(times)
    
    # Display results
    display_player_results(player_id, scores, times, highest_score, average_time)
    
    # Save to file
    save_to_file(player_id, scores, times, highest_score, average_time)
    
    print("\n" + "="*50)
    print("Data recorded successfully!")
    print("="*50)
    input("Press Enter to return to main menu...")

def calculate_highest_score(scores):
    """Finds the highest score in a list of scores"""
    if len(scores) == 0:
        return 0
    return max(scores)

def calculate_average_time(times):
    """Calculates the average time from a list of times"""
    if len(times) == 0:
        return 0.0
    
    total_time = sum(times)
    average = total_time / len(times)
    return round(average, 2)

def display_player_results(player_id, scores, times, highest_score, average_time):
    """Displays all the player statistics in a formatted way"""
    print("\n" + "="*60)
    print("PLAYER STATISTICS SUMMARY")
    print("="*60)
    
    print(f"Player ID: {player_id}")
    print(f"Number of games played: {len(scores)}")
    print(f"Highest Score: {highest_score:,}")
    print(f"Average Time per Game: {average_time} minutes")
    
    print("\n" + "-"*60)
    print("DETAILED GAME DATA")
    print("-"*60)
    
    print("All Scores:")
    for i, score in enumerate(scores, 1):
        print(f"  Game {i}: {score:,} points")
    
    print("\nAll Times:")
    for i, time in enumerate(times, 1):
        print(f"  Game {i}: {time} minutes")
    
    total_time = sum(times)
    print(f"\nTotal Time Played: {total_time} minutes")
    
    print("="*60)

def display_statistics():
    """Function to display previously saved player statistics"""
    print("\n" + "="*50)
    print("DISPLAY SAVED PLAYER STATISTICS")
    print("="*50)
    
    player_id = get_valid_player_id()
    filename = f"player_{player_id}.txt"
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n" + content)
            
    except FileNotFoundError:
        print(f"\nNo data found for player {player_id}")
        print("Make sure you have recorded scores for this player first.")
        
    except Exception as e:
        print(f"Error reading file: {e}")
    
    input("\nPress Enter to return to main menu...")

def save_to_file(player_id, scores, times, highest_score, average_time):
    """Saves all player data to a text file"""
    filename = f"player_{player_id}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("GAMES CLUB STATISTICS REPORT\n")
            file.write("="*40 + "\n")
            file.write(f"Generated for Player: {player_id}\n")
            file.write("="*40 + "\n\n")
            
            file.write("SUMMARY STATISTICS:\n")
            file.write("-"*20 + "\n")
            file.write(f"Player ID: {player_id}\n")
            file.write(f"Number of Games: {len(scores)}\n")
            file.write(f"Highest Score: {highest_score:,}\n")
            file.write(f"Average Time: {average_time} minutes\n")
            file.write(f"Total Time Played: {sum(times)} minutes\n\n")
            
            file.write("DETAILED GAME DATA:\n")
            file.write("-"*20 + "\n")
            
            for i in range(len(scores)):
                file.write(f"Game {i+1}: Score = {scores[i]:,}, Time = {times[i]} minutes\n")
            
            file.write("\n" + "="*40 + "\n")
            file.write("RAW DATA:\n")
            file.write(f"Scores: {', '.join(map(str, scores))}\n")
            file.write(f"Times: {', '.join(map(str, times))}\n")
            
        print(f"\nData successfully saved to: {filename}")
        
    except Exception as e:
        print(f"Error saving file: {e}")
        print("Data could not be saved to file.")

# Run the program
if __name__ == "__main__":
    main()
```

---

## Section 8: How to Use Your Program

### Step 1: Save the Code
1. Copy all the code from Section 7
2. Save it in a file called `games_club_stats.py`
3. Make sure the file extension is `.py`

### Step 2: Run the Program
1. Open your Python environment (IDLE, VS Code, etc.)
2. Run the file
3. The main menu will appear

### Step 3: Test Your Program
Try these test cases:

**Normal Test:**
- Player ID: PLAYER001
- Number of games: 3
- Game 1: Score = 1200, Time = 25.0
- Game 2: Score = 1500, Time = 20.5
- Game 3: Score = 1800, Time = 30.0

**Expected Results:**
- Highest Score: 1,800
- Average Time: 25.17 minutes
- File created: player_PLAYER001.txt

---

## Section 9: Understanding the Output

### Console Output Example:
```
PLAYER STATISTICS SUMMARY
============================================================
Player ID: PLAYER001
Number of games played: 3
Highest Score: 1,800
Average Time per Game: 25.17 minutes

------------------------------------------------------------
DETAILED GAME DATA
------------------------------------------------------------
All Scores:
  Game 1: 1,200 points
  Game 2: 1,500 points
  Game 3: 1,800 points

All Times:
  Game 1: 25.0 minutes
  Game 2: 20.5 minutes
  Game 3: 30.0 minutes

Total Time Played: 75.5 minutes
============================================================
```

### File Output Example (player_PLAYER001.txt):
```
GAMES CLUB STATISTICS REPORT
========================================
Generated for Player: PLAYER001
========================================

SUMMARY STATISTICS:
--------------------
Player ID: PLAYER001
Number of Games: 3
Highest Score: 1,800
Average Time: 25.17 minutes
Total Time Played: 75.5 minutes

DETAILED GAME DATA:
--------------------
Game 1: Score = 1,200, Time = 25.0 minutes
Game 2: Score = 1,500, Time = 20.5 minutes
Game 3: Score = 1,800, Time = 30.0 minutes

========================================
RAW DATA:
Scores: 1200, 1500, 1800
Times: 25.0, 20.5, 30.0
```

---

## Section 10: Testing Your Program

### Test Plan Table
Create this table and fill it out as you test:

| Test # | Purpose | Test Data | Expected Result | Actual Result | Pass/Fail |
|--------|---------|-----------|-----------------|---------------|-----------|
| 1 | Normal data | PLAYER001, 3 games, scores: 100,200,300, times: 10,15,20 | Highest: 300, Average: 15.0 | | |
| 2 | Single game | PLAYER002, 1 game, score: 500, time: 25.5 | Highest: 500, Average: 25.5 | | |
| 3 | Invalid player ID | Empty string | Error message, ask again | | |
| 4 | Invalid score | "abc" | Error message, ask again | | |
| 5 | Negative score | -100 | Error message, ask again | | |
| 6 | Zero time | 0 | Error message, ask again | | |
| 7 | Very large score | 999999 | Accept and display correctly | | |
| 8 | File creation | Any valid data | File created successfully | | |
| 9 | File reading | Existing player | Display saved data | | |
| 10 | File reading | Non-existent player | "No data found" message | | |

---

## Section 11: What Each Part Does (Summary)

1. **Main Function**: Controls the program flow and menu
2. **Input Validation**: Makes sure user enters valid data
3. **Data Recording**: Collects scores and times for each game
4. **Calculations**: Finds highest score and calculates average time
5. **Display**: Shows results in a formatted way
6. **File Handling**: Saves data permanently to text files

---

## Section 12: Key Programming Concepts Used

- **Functions**: Break code into manageable pieces
- **Lists**: Store multiple related values
- **Loops**: Repeat actions (for games, validation)
- **Conditionals**: Make decisions based on data
- **Exception Handling**: Deal with errors gracefully
- **File I/O**: Save and load data permanently
- **String Formatting**: Make output look professional

---

This complete guide gives you all the code you need with detailed explanations. You can copy and paste it section by section, or use the complete program from Section 7. Each part is explained so you understand what it does and why it's needed for your college project.