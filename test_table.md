# Games Club Statistics Program - Test Table

## Test Plan Overview
This document provides a comprehensive test table for validating all functionality of the Games Club Statistics Program. Each test case includes the purpose, test data, expected results, and space to record actual results.

---

## Test Execution Instructions
1. Run each test case in order
2. Record the actual result in the "Actual Result" column
3. Mark Pass/Fail based on whether actual matches expected
4. Note any issues or observations in the "Notes" column

---

## Test Cases Table

| Test # | Test Category | Purpose | Test Data | Expected Result | Actual Result | Pass/Fail | Notes |
|--------|---------------|---------|-----------|-----------------|---------------|-----------|-------|
| **1** | **Input Validation** | Test valid player ID | Player ID: "PLAYER001" | Accept input, convert to uppercase | | | |
| **2** | **Input Validation** | Test empty player ID | Player ID: "" (empty string) | Show error "Oops! You can't leave this empty. Try again." | | | |
| **3** | **Input Validation** | Test long player ID | Player ID: "THISPLAYERIDISTOOLONG123" | Show error "That's too long! Keep it under 20 characters." | | | |
| **4** | **Input Validation** | Test valid number of games | Number of games: 3 | Accept input, return 3 | | | |
| **5** | **Input Validation** | Test zero games | Number of games: 0 | Show error "You need to have played at least 1 game!" | | | |
| **6** | **Input Validation** | Test negative games | Number of games: -5 | Show error "You need to have played at least 1 game!" | | | |
| **7** | **Input Validation** | Test too many games | Number of games: 150 | Show error "Wow, that's a lot! Let's keep it under 100 games." | | | |
| **8** | **Input Validation** | Test non-numeric games | Number of games: "abc" | Show error "Please enter a number, not letters!" | | | |
| **9** | **Input Validation** | Test valid score | Score: 1500 | Accept input, return 1500 | | | |
| **10** | **Input Validation** | Test zero score | Score: 0 | Accept input, return 0 | | | |
| **11** | **Input Validation** | Test negative score | Score: -100 | Show error "Scores can't be negative! Try again." | | | |
| **12** | **Input Validation** | Test very high score | Score: 2000000 | Show error "That's an amazing score, but let's keep it under 1,000,000!" | | | |
| **13** | **Input Validation** | Test non-numeric score | Score: "xyz" | Show error "Please enter a number for the score!" | | | |
| **14** | **Input Validation** | Test valid time | Time: 25.5 | Accept input, return 25.5 | | | |
| **15** | **Input Validation** | Test zero time | Time: 0 | Show error "Time must be more than 0 minutes!" | | | |
| **16** | **Input Validation** | Test negative time | Time: -10.5 | Show error "Time must be more than 0 minutes!" | | | |
| **17** | **Input Validation** | Test very long time | Time: 2000 | Show error "That's more than 24 hours! Are you sure?" | | | |
| **18** | **Input Validation** | Test non-numeric time | Time: "abc" | Show error "Please enter a number for the time!" | | | |
| **19** | **Calculations** | Test highest score calculation | Scores: [100, 200, 300] | Return 300 | | | |
| **20** | **Calculations** | Test highest score with single value | Scores: [500] | Return 500 | | | |
| **21** | **Calculations** | Test highest score with empty list | Scores: [] | Return 0 | | | |
| **22** | **Calculations** | Test average time calculation | Times: [10.0, 20.0, 30.0] | Return 20.0 | | | |
| **23** | **Calculations** | Test average time with decimals | Times: [10.5, 15.5, 20.0] | Return 15.33 | | | |
| **24** | **Calculations** | Test average time with single value | Times: [25.5] | Return 25.5 | | | |
| **25** | **Calculations** | Test average time with empty list | Times: [] | Return 0.0 | | | |
| **26** | **Display** | Test results display format | Player: "TEST001", Scores: [1000, 1500], Times: [20.0, 25.0] | Show formatted statistics with player ID, games count, highest score, average time | | | |
| **27** | **Display** | Test score formatting with commas | Score: 1234567 | Display as "1,234,567" | | | |
| **28** | **File Operations** | Test file creation | Valid player data | Create file "player_PLAYERID.txt" | | | |
| **29** | **File Operations** | Test file content format | Valid player data | File contains header, summary, detailed data, raw data | | | |
| **30** | **File Operations** | Test file reading existing player | Existing file "player_TEST001.txt" | Display file contents | | | |
| **31** | **File Operations** | Test file reading non-existent player | Player ID: "NONEXISTENT" | Show "Sorry, no data found for player NONEXISTENT" | | | |
| **32** | **Integration** | Test complete workflow - single game | Player: "SINGLE001", Games: 1, Score: 1000, Time: 30.0 | Complete process, show results, save file | | | |
| **33** | **Integration** | Test complete workflow - multiple games | Player: "MULTI001", Games: 3, Scores: [800, 1200, 1600], Times: [15.0, 20.0, 25.0] | Complete process, highest=1600, average=20.0 | | | |
| **34** | **Menu System** | Test menu choice 1 | Menu choice: "1" | Go to record scores function | | | |
| **35** | **Menu System** | Test menu choice 2 | Menu choice: "2" | Go to show saved stats function | | | |
| **36** | **Menu System** | Test menu choice 3 | Menu choice: "3" | Exit program with goodbye message | | | |
| **37** | **Menu System** | Test invalid menu choice | Menu choice: "5" | Show error "That's not a valid choice. Please pick 1, 2, or 3." | | | |
| **38** | **Edge Cases** | Test maximum valid score | Score: 1000000 | Accept input, return 1000000 | | | |
| **39** | **Edge Cases** | Test maximum valid time | Time: 1440.0 | Accept input, return 1440.0 | | | |
| **40** | **Edge Cases** | Test maximum valid games | Games: 100 | Accept input, return 100 | | | |

---

## Sample Test Data Sets

### Test Set 1: Normal Usage
- **Player ID**: "PLAYER001"
- **Number of Games**: 3
- **Game 1**: Score = 1200, Time = 25.0
- **Game 2**: Score = 1500, Time = 20.5  
- **Game 3**: Score = 1800, Time = 30.0
- **Expected Results**: Highest = 1,800, Average = 25.17 minutes

### Test Set 2: Single Game
- **Player ID**: "SINGLE"
- **Number of Games**: 1
- **Game 1**: Score = 2500, Time = 45.5
- **Expected Results**: Highest = 2,500, Average = 45.5 minutes

### Test Set 3: Many Games
- **Player ID**: "MANYGAMES"
- **Number of Games**: 5
- **Scores**: [500, 750, 1000, 1250, 1500]
- **Times**: [10.0, 15.0, 20.0, 25.0, 30.0]
- **Expected Results**: Highest = 1,500, Average = 20.0 minutes

### Test Set 4: Edge Case Values
- **Player ID**: "EDGE"
- **Number of Games**: 2
- **Game 1**: Score = 0, Time = 0.1
- **Game 2**: Score = 1000000, Time = 1440.0
- **Expected Results**: Highest = 1,000,000, Average = 720.05 minutes

---

## File Content Verification Checklist

When testing file operations, verify the saved file contains:

- [ ] **Header Section**
  - [ ] "GAMES CLUB STATISTICS REPORT"
  - [ ] Separator line (40 equals signs)
  - [ ] "Report for Player: [PLAYER_ID]"
  - [ ] Separator line (40 equals signs)

- [ ] **Summary Section**
  - [ ] "SUMMARY:" header
  - [ ] Separator line (20 dashes)
  - [ ] Player ID
  - [ ] Number of Games
  - [ ] Highest Score (with comma formatting)
  - [ ] Average Time
  - [ ] Total Time Played

- [ ] **Detailed Data Section**
  - [ ] "DETAILED GAME DATA:" header
  - [ ] Separator line (20 dashes)
  - [ ] Each game listed with score and time
  - [ ] Proper game numbering (1, 2, 3...)

- [ ] **Raw Data Section**
  - [ ] Separator line (40 equals signs)
  - [ ] "RAW DATA:" header
  - [ ] Scores line with comma-separated values
  - [ ] Times line with comma-separated values

---

## Error Handling Test Cases

| Error Type | Test Scenario | Expected Behavior |
|------------|---------------|-------------------|
| **File Permission** | Try to save to read-only directory | Show error message, continue program |
| **Disk Full** | Save file when disk is full | Show error message, continue program |
| **Invalid Characters** | Player ID with special characters | Accept input (program allows special chars) |
| **Very Long Input** | Extremely long player ID | Show length error message |
| **Decimal Games** | Enter 2.5 for number of games | Show "Please enter a number" error |
| **Scientific Notation** | Enter 1e6 for score | Should accept as 1000000 |

---

## Performance Test Cases

| Test | Scenario | Expected Performance |
|------|----------|---------------------|
| **P1** | Process 100 games | Complete within reasonable time |
| **P2** | Save large file (100 games) | File saves successfully |
| **P3** | Read large file | File displays correctly |
| **P4** | Multiple file operations | No memory issues |

---

## Test Completion Summary

**Total Test Cases**: 40 core tests + error handling + performance  
**Categories Covered**:
- Input Validation (18 tests)
- Calculations (7 tests)
- Display Functions (3 tests)
- File Operations (4 tests)
- Integration Tests (3 tests)
- Menu System (5 tests)

**Test Execution Date**: _______________  
**Tester Name**: _______________  
**Overall Result**: _______________  
**Issues Found**: _______________  
**Recommendations**: _______________

---

## Notes Section
Use this space to record any additional observations, bugs found, or suggestions for improvement:

```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________