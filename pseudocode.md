# Games Club Statistics Program - Python-Style Pseudocode

## Program Overview
This pseudocode describes the structure and logic of the Computer Games Club Statistics Program written in basic Python for high school level.

---

## Main Program Structure

```python
# Main Program Entry Point
def main():
    print("Welcome to Games Club Statistics Program")
    
    # Main program loop - keeps running until user exits
    while True:
        choice = show_menu()
        
        if choice == "1":
            record_scores()
        elif choice == "2":
            show_saved_stats()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")

# Program starts here
if __name__ == "__main__":
    main()
```

---

## Menu System

```python
def show_menu():
    """Display main menu and get user choice"""
    print("GAMES CLUB STATISTICS PROGRAM")
    print("1. Record Player Scores")
    print("2. Show Saved Player Stats") 
    print("3. Exit Program")
    
    choice = input("What would you like to do? (1-3): ")
    return choice
```

---

## Input Validation Functions

```python
def get_player_id():
    """Get valid player ID with validation"""
    while True:
        player_id = input("Enter Player ID: ").strip()
        
        if len(player_id) == 0:
            print("Error: Cannot be empty")
        elif len(player_id) > 20:
            print("Error: Too long (max 20 characters)")
        else:
            return player_id.upper()  # Convert to uppercase

def get_number_of_games():
    """Get valid number of games with validation"""
    while True:
        try:
            num_games = int(input("How many games did you play? "))
            
            if num_games <= 0:
                print("Error: Must be at least 1 game")
            elif num_games > 100:
                print("Error: Too many games (max 100)")
            else:
                return num_games
        except ValueError:
            print("Error: Please enter a number")

def get_time():
    """Get valid time with validation"""
    while True:
        try:
            time = float(input("How long did you play (in minutes)? "))
            
            if time <= 0:
                print("Error: Time must be positive")
            elif time > 1440:  # 24 hours in minutes
                print("Error: Time too long (max 24 hours)")
            else:
                return time
        except ValueError:
            print("Error: Please enter a number")
```

---

## Main Data Recording Function

```python
def record_scores():
    """Main function to record all player data"""
    print("RECORD PLAYER SCORES")
    
    # Step 1: Get basic player information
    player_id = get_player_id()
    num_games = get_number_of_games()
    
    # Step 2: Initialize empty lists for data storage
    scores = []  # List to store all scores
    times = []   # List to store all times
    
    # Step 3: Collect data for each game
    print(f"Entering data for {num_games} games:")
    
    for game_number in range(1, num_games + 1):
        print(f"Game {game_number}:")
        
        # Get score and time for this game
        score = get_score()
        time = get_time()
        
        # Add to lists
        scores.append(score)
        times.append(time)
        
        print(f"Recorded: Score = {score}, Time = {time} minutes")
    
    # Step 4: Calculate statistics
    print("Calculating statistics...")
    highest_score = find_highest_score(scores)
    average_time = calculate_average_time(times)
    
    # Step 5: Display results
    show_results(player_id, scores, times, highest_score, average_time)
    
    # Step 6: Save to file
    save_to_file(player_id, scores, times, highest_score, average_time)
    
    print("Data recorded successfully!")
    input("Press Enter to return to main menu...")
```

---

## Calculation Functions

```python
def find_highest_score(scores):
    """Find the highest score in a list"""
    if len(scores) == 0:
        return 0
    
    # Use built-in max() function
    return max(scores)

def calculate_average_time(times):
    """Calculate average time from a list of times"""
    if len(times) == 0:
        return 0.0
    
    # Calculate average: sum divided by count
    total_time = sum(times)
    average = total_time / len(times)
    
    # Round to 2 decimal places
    return round(average, 2)
```

---

## Display Functions

```python
def show_results(player_id, scores, times, highest_score, average_time):
    """Display all player statistics in formatted way"""
    print("YOUR GAME STATISTICS")
    print("=" * 60)
    
    # Basic statistics
    print(f"Player ID: {player_id}")
    print(f"Number of games played: {len(scores)}")
    print(f"Highest Score: {highest_score:,}")  # Format with commas
    print(f"Average Time per Game: {average_time} minutes")
    
    print("ALL YOUR GAME DATA")
    print("-" * 60)
    
    # Show all scores
    print("All Your Scores:")
    for i in range(len(scores)):
        game_num = i + 1  # Start from Game 1, not Game 0
        print(f"  Game {game_num}: {scores[i]:,} points")
    
    # Show all times
    print("All Your Times:")
    for i in range(len(times)):
        game_num = i + 1
        print(f"  Game {game_num}: {times[i]} minutes")
    
    # Show total time
    total_time = sum(times)
    print(f"Total Time Played: {total_time} minutes")
```

---

## File Operations

```python
def save_to_file(player_id, scores, times, highest_score, average_time):
    """Save all player data to a text file"""
    filename = f"player_{player_id}.txt"
    
    try:
        # Open file for writing
        with open(filename, 'w') as file:
            
            # Write header
            file.write("GAMES CLUB STATISTICS REPORT\n")
            file.write("=" * 40 + "\n")
            file.write(f"Report for Player: {player_id}\n")
            file.write("=" * 40 + "\n\n")
            
            # Write summary statistics
            file.write("SUMMARY:\n")
            file.write("-" * 20 + "\n")
            file.write(f"Player ID: {player_id}\n")
            file.write(f"Number of Games: {len(scores)}\n")
            file.write(f"Highest Score: {highest_score:,}\n")
            file.write(f"Average Time: {average_time} minutes\n")
            file.write(f"Total Time Played: {sum(times)} minutes\n\n")
            
            # Write detailed game data
            file.write("DETAILED GAME DATA:\n")
            file.write("-" * 20 + "\n")
            
            for i in range(len(scores)):
                game_num = i + 1
                file.write(f"Game {game_num}: Score = {scores[i]:,}, Time = {times[i]} minutes\n")
            
            file.write("\n" + "=" * 40 + "\n")
            
            # Write raw data for potential reuse
            file.write("RAW DATA:\n")
            scores_text = ', '.join([str(score) for score in scores])
            times_text = ', '.join([str(time) for time in times])
            file.write(f"Scores: {scores_text}\n")
            file.write(f"Times: {times_text}\n")
            
        print(f"Data saved to: {filename}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

def show_saved_stats():
    """Display previously saved player statistics"""
    print("SHOW SAVED PLAYER STATS")
    
    # Get player ID to look up
    player_id = get_player_id()
    filename = f"player_{player_id}.txt"
    
    try:
        # Try to read the file
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            
    except FileNotFoundError:
        print(f"No data found for player {player_id}")
        print("Make sure you've recorded scores for this player first!")
        
    except Exception as e:
        print(f"Error reading file: {e}")
    
    input("Press Enter to return to main menu...")
```

---

## Program Flow Logic

### Overall Program Flow:
1. **START** → Display welcome message
2. **LOOP** → Show main menu
3. **INPUT** → Get user choice (1, 2, or 3)
4. **BRANCH**:
   - Choice 1 → Go to record_scores()
   - Choice 2 → Go to show_saved_stats()  
   - Choice 3 → Exit program
   - Invalid → Show error, return to menu
5. **REPEAT** → Continue loop until user exits

### Record Scores Flow:
1. **INPUT** → Get player ID (with validation)
2. **INPUT** → Get number of games (with validation)
3. **INITIALIZE** → Create empty lists for scores and times
4. **LOOP** → For each game:
   - Get score (with validation)
   - Get time (with validation)
   - Add to lists
5. **CALCULATE** → Find highest score and average time
6. **DISPLAY** → Show formatted results
7. **SAVE** → Write data to file
8. **RETURN** → Back to main menu

### Show Saved Stats Flow:
1. **INPUT** → Get player ID (with validation)
2. **TRY** → Open and read player file
3. **DISPLAY** → Show file contents
4. **CATCH** → Handle file not found or other errors
5. **RETURN** → Back to main menu

---

## Data Structures Used

```python
# Lists for storing game data
scores = [1200, 1500, 1800]  # List of integers
times = [25.0, 20.5, 30.0]   # List of floats

# Variables for calculations
highest_score = int          # Single integer value
average_time = float         # Single float value (rounded to 2 decimals)
player_id = string          # String (converted to uppercase)
num_games = int             # Positive integer

# File operations
filename = string           # Format: "player_PLAYERID.txt"
file_content = string       # Complete file content as text
```

---

## Error Handling Strategy

```python
# Input validation pattern used throughout:
while True:
    try:
        # Get user input
        # Convert to appropriate type (int, float)
        # Validate range/constraints
        # Return valid value
    except ValueError:
        # Handle conversion errors
        print("Error message")
        # Continue loop to ask again

# File operation pattern:
try:
    # File operations (open, read, write)
except FileNotFoundError:
    # Handle missing files
except Exception as e:
    # Handle other file errors
```

---

## Key Programming Concepts Demonstrated

1. **Functions**: Modular code organization
2. **Loops**: `while` for validation, `for` for iteration
3. **Lists**: Dynamic data storage with `append()`
4. **Conditionals**: `if/elif/else` for decision making
5. **Exception Handling**: `try/except` for error management
6. **File I/O**: Reading and writing text files
7. **String Formatting**: f-strings and format specifiers
8. **Input Validation**: Ensuring data quality
9. **Built-in Functions**: `max()`, `sum()`, `len()`, `round()`
10. **Type Conversion**: `int()`, `float()`, `str()`

This pseudocode represents a complete, functional program suitable for high school level Python programming education.