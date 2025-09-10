# Games Club Statistics Program - Test Table

## Test Plan Overview
This document provides a comprehensive test table for validating all functionality of the Games Club Statistics Program. Each test case includes the purpose, test data, expected results, and space to record actual results.

## Test Cases Table

| Test # | Test Category | Purpose | Test Data | Expected Result | Actual Result | Pass/Fail | Notes |
|--------|---------------|---------|-----------|-----------------|---------------|-----------|-------|
| **1** | **Input Validation** | Test valid player ID | Player ID: "PLAYER001" | Accept input, convert to uppercase | Input accepted, converted to "PLAYER001" | **PASS** | Automated test verified |
| **2** | **Input Validation** | Test empty player ID | Player ID: "" (empty string) | Show error "Oops! You can't leave this empty. Try again." | Error message displayed correctly | **PASS** | Automated test verified |
| **3** | **Input Validation** | Test long player ID | Player ID: "THISPLAYERIDISTOOLONG123" | Show error "That's too long! Keep it under 20 characters." | Error message displayed correctly | **PASS** | Automated test verified |
| **4** | **Input Validation** | Test valid number of games | Number of games: 3 | Accept input, return 3 | Input accepted, returned 3 | **PASS** | Automated test verified |
| **5** | **Input Validation** | Test zero games | Number of games: 0 | Show error "You need to have played at least 1 game!" | Error message displayed correctly | **PASS** | Automated test verified |
| **6** | **Input Validation** | Test negative games | Number of games: -5 | Show error "You need to have played at least 1 game!" | Error message displayed correctly | **PASS** | Automated test verified |
| **7** | **Input Validation** | Test too many games | Number of games: 150 | Show error "Wow, that's a lot! Let's keep it under 100 games." | Error message displayed correctly | **PASS** | Automated test verified |
| **8** | **Input Validation** | Test non-numeric games | Number of games: "abc" | Show error "Please enter a number, not letters!" | Error message displayed correctly | **PASS** | Automated test verified |
| **9** | **Input Validation** | Test valid score | Score: 1500 | Accept input, return 1500 | Input accepted, returned 1500 | **PASS** | Automated test verified |
| **10** | **Input Validation** | Test zero score | Score: 0 | Accept input, return 0 | Input accepted, returned 0 | **PASS** | Automated test verified |
| **11** | **Input Validation** | Test negative score | Score: -100 | Show error "Scores can't be negative! Try again." | Error message displayed correctly | **PASS** | Automated test verified |
| **12** | **Input Validation** | Test very high score | Score: 2000000 | Show error "That's an amazing score, but let's keep it under 1,000,000!" | Error message displayed correctly | **PASS** | Automated test verified |
| **13** | **Input Validation** | Test non-numeric score | Score: "xyz" | Show error "Please enter a number for the score!" | Error message displayed correctly | **PASS** | Automated test verified |
| **14** | **Input Validation** | Test valid time | Time: 25.5 | Accept input, return 25.5 | Input accepted, returned 25.5 | **PASS** | Automated test verified |
| **15** | **Input Validation** | Test zero time | Time: 0 | Show error "Time must be more than 0 minutes!" | Error message displayed correctly | **PASS** | Automated test verified |
| **16** | **Input Validation** | Test negative time | Time: -10.5 | Show error "Time must be more than 0 minutes!" | Error message displayed correctly | **PASS** | Automated test verified |
| **17** | **Input Validation** | Test very long time | Time: 2000 | Show error "That's more than 24 hours! Are you sure?" | Error message displayed correctly | **PASS** | Automated test verified |
| **18** | **Input Validation** | Test non-numeric time | Time: "abc" | Show error "Please enter a number for the time!" | Error message displayed correctly | **PASS** | Automated test verified |
| **19** | **Calculations** | Test highest score calculation | Scores: [100, 200, 300] | Return 300 | Returned 300 | **PASS** | Automated test verified |
| **20** | **Calculations** | Test highest score with single value | Scores: [500] | Return 500 | Returned 500 | **PASS** | Automated test verified |
| **21** | **Calculations** | Test highest score with empty list | Scores: [] | Return 0 | Returned 0 | **PASS** | Automated test verified |
| **22** | **Calculations** | Test average time calculation | Times: [10.0, 20.0, 30.0] | Return 20.0 | Returned 20.0 | **PASS** | Automated test verified |
| **23** | **Calculations** | Test average time with decimals | Times: [10.5, 15.5, 20.0] | Return 15.33 | Returned 15.33 | **PASS** | Automated test verified |
| **24** | **Calculations** | Test average time with single value | Times: [25.5] | Return 25.5 | Returned 25.5 | **PASS** | Automated test verified |
| **25** | **Calculations** | Test average time with empty list | Times: [] | Return 0.0 | Returned 0.0 | **PASS** | Automated test verified |
| **26** | **Display** | Test results display format | Player: "TEST001", Scores: [1000, 1500], Times: [20.0, 25.0] | Show formatted statistics with player ID, games count, highest score, average time | Statistics displayed correctly | **PASS** | Automated test verified |
| **27** | **Display** | Test score formatting with commas | Score: 1234567 | Display as "1,234,567" | Formatted as "1,234,567" | **PASS** | Automated test verified |
| **28** | **File Operations** | Test file creation | Valid player data | Create file "player_PLAYERID.txt" | File created successfully | **PASS** | Automated test verified |
| **29** | **File Operations** | Test file content format | Valid player data | File contains header, summary, detailed data, raw data | File format verified correct | **PASS** | Automated test verified |
| **30** | **File Operations** | Test file reading existing player | Existing file "player_TEST001.txt" | Display file contents | File contents displayed | **PASS** | Automated test verified |
| **31** | **File Operations** | Test file reading non-existent player | Player ID: "NONEXISTENT" | Show "Sorry, no data found for player NONEXISTENT" | Error message displayed correctly | **PASS** | Automated test verified |
| **32** | **Integration** | Test complete workflow - single game | Player: "SINGLE001", Games: 1, Score: 1000, Time: 30.0 | Complete process, show results, save file | Workflow completed successfully | **PASS** | Automated test verified |
| **33** | **Integration** | Test complete workflow - multiple games | Player: "MULTI001", Games: 3, Scores: [800, 1200, 1600], Times: [15.0, 20.0, 25.0] | Complete process, highest=1600, average=20.0 | Workflow completed successfully | **PASS** | Automated test verified |
| **34** | **Menu System** | Test menu choice 1 | Menu choice: "1" | Go to record scores function | Menu choice handled correctly | **PASS** | Automated test verified |
| **35** | **Menu System** | Test menu choice 2 | Menu choice: "2" | Go to show saved stats function | Menu choice handled correctly | **PASS** | Automated test verified |
| **36** | **Menu System** | Test menu choice 3 | Menu choice: "3" | Exit program with goodbye message | Menu choice handled correctly | **PASS** | Automated test verified |
| **37** | **Menu System** | Test invalid menu choice | Menu choice: "5" | Show error "That's not a valid choice. Please pick 1, 2, or 3." | Error handled in main loop | **PASS** | Tested via integration |
| **38** | **Edge Cases** | Test maximum valid score | Score: 1000000 | Accept input, return 1000000 | Input accepted, returned 1000000 | **PASS** | Automated test verified |
| **39** | **Edge Cases** | Test maximum valid time | Time: 1440.0 | Accept input, return 1440.0 | Input accepted, returned 1440.0 | **PASS** | Automated test verified |
| **40** | **Edge Cases** | Test maximum valid games | Games: 100 | Accept input, return 100 | Input accepted, returned 100 | **PASS** | Automated test verified |