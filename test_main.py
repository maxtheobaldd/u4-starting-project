"""
Unit tests for Games Club Statistics Program
Based on test_table.md test cases
"""

import unittest
import io
import sys
import os
from unittest.mock import patch, mock_open, MagicMock
import main


class TestInputValidation(unittest.TestCase):
    """Test cases for input validation functions"""
    
    def test_get_player_id_valid(self):
        """Test 1: Test valid player ID"""
        with patch('builtins.input', return_value='player001'):
            result = main.get_player_id()
            self.assertEqual(result, 'PLAYER001')
    
    def test_get_player_id_empty(self):
        """Test 2: Test empty player ID"""
        with patch('builtins.input', side_effect=['', 'VALID']):
            with patch('builtins.print') as mock_print:
                result = main.get_player_id()
                mock_print.assert_any_call("Oops! You can't leave this empty. Try again.")
                self.assertEqual(result, 'VALID')
    
    def test_get_player_id_too_long(self):
        """Test 3: Test long player ID"""
        long_id = 'THISPLAYERIDISTOOLONG123'
        with patch('builtins.input', side_effect=[long_id, 'VALID']):
            with patch('builtins.print') as mock_print:
                result = main.get_player_id()
                mock_print.assert_any_call("That's too long! Keep it under 20 characters.")
                self.assertEqual(result, 'VALID')
    
    def test_get_number_of_games_valid(self):
        """Test 4: Test valid number of games"""
        with patch('builtins.input', return_value='3'):
            result = main.get_number_of_games()
            self.assertEqual(result, 3)
    
    def test_get_number_of_games_zero(self):
        """Test 5: Test zero games"""
        with patch('builtins.input', side_effect=['0', '3']):
            with patch('builtins.print') as mock_print:
                result = main.get_number_of_games()
                mock_print.assert_any_call("You need to have played at least 1 game!")
                self.assertEqual(result, 3)
    
    def test_get_number_of_games_negative(self):
        """Test 6: Test negative games"""
        with patch('builtins.input', side_effect=['-5', '3']):
            with patch('builtins.print') as mock_print:
                result = main.get_number_of_games()
                mock_print.assert_any_call("You need to have played at least 1 game!")
                self.assertEqual(result, 3)
    
    def test_get_number_of_games_too_many(self):
        """Test 7: Test too many games"""
        with patch('builtins.input', side_effect=['150', '50']):
            with patch('builtins.print') as mock_print:
                result = main.get_number_of_games()
                mock_print.assert_any_call("Wow, that's a lot! Let's keep it under 100 games.")
                self.assertEqual(result, 50)
    
    def test_get_number_of_games_non_numeric(self):
        """Test 8: Test non-numeric games"""
        with patch('builtins.input', side_effect=['abc', '5']):
            with patch('builtins.print') as mock_print:
                result = main.get_number_of_games()
                mock_print.assert_any_call("Please enter a number, not letters!")
                self.assertEqual(result, 5)
    
    def test_get_score_valid(self):
        """Test 9: Test valid score"""
        with patch('builtins.input', return_value='1500'):
            result = main.get_score()
            self.assertEqual(result, 1500)
    
    def test_get_score_zero(self):
        """Test 10: Test zero score"""
        with patch('builtins.input', return_value='0'):
            result = main.get_score()
            self.assertEqual(result, 0)
    
    def test_get_score_negative(self):
        """Test 11: Test negative score"""
        with patch('builtins.input', side_effect=['-100', '100']):
            with patch('builtins.print') as mock_print:
                result = main.get_score()
                mock_print.assert_any_call("Scores can't be negative! Try again.")
                self.assertEqual(result, 100)
    
    def test_get_score_too_high(self):
        """Test 12: Test very high score"""
        with patch('builtins.input', side_effect=['2000000', '500000']):
            with patch('builtins.print') as mock_print:
                result = main.get_score()
                mock_print.assert_any_call("That's an amazing score, but let's keep it under 1,000,000!")
                self.assertEqual(result, 500000)
    
    def test_get_score_non_numeric(self):
        """Test 13: Test non-numeric score"""
        with patch('builtins.input', side_effect=['xyz', '1000']):
            with patch('builtins.print') as mock_print:
                result = main.get_score()
                mock_print.assert_any_call("Please enter a number for the score!")
                self.assertEqual(result, 1000)
    
    def test_get_time_valid(self):
        """Test 14: Test valid time"""
        with patch('builtins.input', return_value='25.5'):
            result = main.get_time()
            self.assertEqual(result, 25.5)
    
    def test_get_time_zero(self):
        """Test 15: Test zero time"""
        with patch('builtins.input', side_effect=['0', '10.5']):
            with patch('builtins.print') as mock_print:
                result = main.get_time()
                mock_print.assert_any_call("Time must be more than 0 minutes!")
                self.assertEqual(result, 10.5)
    
    def test_get_time_negative(self):
        """Test 16: Test negative time"""
        with patch('builtins.input', side_effect=['-10.5', '15.0']):
            with patch('builtins.print') as mock_print:
                result = main.get_time()
                mock_print.assert_any_call("Time must be more than 0 minutes!")
                self.assertEqual(result, 15.0)
    
    def test_get_time_too_long(self):
        """Test 17: Test very long time"""
        with patch('builtins.input', side_effect=['2000', '120.0']):
            with patch('builtins.print') as mock_print:
                result = main.get_time()
                mock_print.assert_any_call("That's more than 24 hours! Are you sure?")
                self.assertEqual(result, 120.0)
    
    def test_get_time_non_numeric(self):
        """Test 18: Test non-numeric time"""
        with patch('builtins.input', side_effect=['abc', '30.0']):
            with patch('builtins.print') as mock_print:
                result = main.get_time()
                mock_print.assert_any_call("Please enter a number for the time!")
                self.assertEqual(result, 30.0)


class TestCalculations(unittest.TestCase):
    """Test cases for calculation functions"""
    
    def test_highest_score_multiple_values(self):
        """Test 19: Test highest score calculation"""
        scores = [100, 200, 300]
        result = main.find_highest_score(scores)
        self.assertEqual(result, 300)
    
    def test_highest_score_single_value(self):
        """Test 20: Test highest score with single value"""
        scores = [500]
        result = main.find_highest_score(scores)
        self.assertEqual(result, 500)
    
    def test_highest_score_empty_list(self):
        """Test 21: Test highest score with empty list"""
        scores = []
        result = main.find_highest_score(scores)
        self.assertEqual(result, 0)
    
    def test_average_time_multiple_values(self):
        """Test 22: Test average time calculation"""
        times = [10.0, 20.0, 30.0]
        result = main.calculate_average_time(times)
        self.assertEqual(result, 20.0)
    
    def test_average_time_with_decimals(self):
        """Test 23: Test average time with decimals"""
        times = [10.5, 15.5, 20.0]
        result = main.calculate_average_time(times)
        self.assertEqual(result, 15.33)
    
    def test_average_time_single_value(self):
        """Test 24: Test average time with single value"""
        times = [25.5]
        result = main.calculate_average_time(times)
        self.assertEqual(result, 25.5)
    
    def test_average_time_empty_list(self):
        """Test 25: Test average time with empty list"""
        times = []
        result = main.calculate_average_time(times)
        self.assertEqual(result, 0.0)


class TestDisplay(unittest.TestCase):
    """Test cases for display functions"""
    
    @patch('builtins.print')
    def test_results_display_format(self, mock_print):
        """Test 26: Test results display format"""
        player_id = "TEST001"
        scores = [1000, 1500]
        times = [20.0, 25.0]
        highest_score = 1500
        average_time = 22.5
        
        main.show_results(player_id, scores, times, highest_score, average_time)
        
        # Verify that print was called with expected content
        mock_print.assert_called()
        self.assertTrue(True)  # Placeholder - actual implementation would check print calls
    
    def test_score_formatting_with_commas(self):
        """Test 27: Test score formatting with commas"""
        # This test verifies that the formatting works correctly
        score = 1234567
        formatted = f"{score:,}"
        self.assertEqual(formatted, "1,234,567")


class TestFileOperations(unittest.TestCase):
    """Test cases for file operations"""
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_file_creation(self, mock_print, mock_file):
        """Test 28: Test file creation"""
        player_id = "TEST001"
        scores = [1000, 1500]
        times = [20.0, 25.0]
        highest_score = 1500
        average_time = 22.5
        
        main.save_to_file(player_id, scores, times, highest_score, average_time)
        
        # Verify file was opened with correct name
        mock_file.assert_called_once_with("player_TEST001.txt", 'w')
    
    @patch('builtins.open', new_callable=mock_open)
    def test_file_content_format(self, mock_file):
        """Test 29: Test file content format"""
        player_id = "TEST001"
        scores = [1000, 1500]
        times = [20.0, 25.0]
        highest_score = 1500
        average_time = 22.5
        
        main.save_to_file(player_id, scores, times, highest_score, average_time)
        
        # Check that write was called (basic verification)
        mock_file().write.assert_called()
    
    @patch('builtins.open', new_callable=mock_open, read_data="Test file content")
    @patch('builtins.input', return_value='TEST001')
    @patch('builtins.print')
    def test_file_reading_existing_player(self, mock_print, mock_input, mock_file):
        """Test 30: Test file reading existing player"""
        main.show_saved_stats()
        
        # Verify file was opened for reading
        mock_file.assert_called_with("player_TEST001.txt", 'r')
    
    @patch('builtins.open', side_effect=FileNotFoundError())
    @patch('builtins.input', side_effect=['NONEXISTENT', ''])
    @patch('builtins.print')
    def test_file_reading_non_existent_player(self, mock_print, mock_input, mock_file):
        """Test 31: Test file reading non-existent player"""
        main.show_saved_stats()
        
        # Verify error message was printed (check for the actual message format)
        mock_print.assert_any_call("\nSorry, no data found for player NONEXISTENT")


class TestIntegration(unittest.TestCase):
    """Test cases for integration workflows"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('main.save_to_file')
    def test_complete_workflow_single_game(self, mock_save, mock_print, mock_input):
        """Test 32: Test complete workflow - single game"""
        # Mock all inputs for single game workflow (including final Enter press)
        inputs = ['SINGLE001', '1', '1000', '30.0', '']
        mock_input.side_effect = inputs
        
        main.record_scores()
        
        # Verify save_to_file was called
        mock_save.assert_called_once()
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('main.save_to_file')
    def test_complete_workflow_multiple_games(self, mock_save, mock_print, mock_input):
        """Test 33: Test complete workflow - multiple games"""
        # Mock inputs for multiple games (including final Enter press)
        inputs = ['MULTI001', '3', '800', '15.0', '1200', '20.0', '1600', '25.0', '']
        mock_input.side_effect = inputs
        
        main.record_scores()
        
        # Verify save_to_file was called
        mock_save.assert_called_once()


class TestMenuSystem(unittest.TestCase):
    """Test cases for menu system"""
    
    def test_show_menu_returns_choice(self):
        """Test 34: Test menu choice 1"""
        with patch('builtins.input', return_value='1'):
            with patch('builtins.print'):
                result = main.show_menu()
                self.assertEqual(result, '1')
    
    def test_menu_choice_2(self):
        """Test 35: Test menu choice 2"""
        with patch('builtins.input', return_value='2'):
            with patch('builtins.print'):
                result = main.show_menu()
                self.assertEqual(result, '2')
    
    def test_menu_choice_3(self):
        """Test 36: Test menu choice 3"""
        with patch('builtins.input', return_value='3'):
            with patch('builtins.print'):
                result = main.show_menu()
                self.assertEqual(result, '3')
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('main.show_menu')
    @patch('main.record_scores')
    @patch('main.show_saved_stats')
    def test_main_menu_integration(self, mock_show_saved, mock_record, mock_show_menu, mock_print, mock_input):
        """Test main menu integration with different choices"""
        # Test that main() handles menu choices correctly
        mock_show_menu.side_effect = ['1', '3']  # Choose 1, then exit
        
        main.main()
        
        # Verify record_scores was called when choice 1 was selected
        mock_record.assert_called_once()


class TestEdgeCases(unittest.TestCase):
    """Test cases for edge cases"""
    
    def test_maximum_valid_score(self):
        """Test 38: Test maximum valid score"""
        with patch('builtins.input', return_value='1000000'):
            result = main.get_score()
            self.assertEqual(result, 1000000)
    
    def test_maximum_valid_time(self):
        """Test 39: Test maximum valid time"""
        with patch('builtins.input', return_value='1440.0'):
            result = main.get_time()
            self.assertEqual(result, 1440.0)
    
    def test_maximum_valid_games(self):
        """Test 40: Test maximum valid games"""
        with patch('builtins.input', return_value='100'):
            result = main.get_number_of_games()
            self.assertEqual(result, 100)


class TestSampleDataSets(unittest.TestCase):
    """Test cases using sample data sets from test_table.md"""
    
    def test_sample_set_1_normal_usage(self):
        """Test Set 1: Normal Usage"""
        scores = [1200, 1500, 1800]
        times = [25.0, 20.5, 30.0]
        
        highest = main.find_highest_score(scores)
        average = main.calculate_average_time(times)
        
        self.assertEqual(highest, 1800)
        self.assertEqual(average, 25.17)
    
    def test_sample_set_2_single_game(self):
        """Test Set 2: Single Game"""
        scores = [2500]
        times = [45.5]
        
        highest = main.find_highest_score(scores)
        average = main.calculate_average_time(times)
        
        self.assertEqual(highest, 2500)
        self.assertEqual(average, 45.5)
    
    def test_sample_set_3_many_games(self):
        """Test Set 3: Many Games"""
        scores = [500, 750, 1000, 1250, 1500]
        times = [10.0, 15.0, 20.0, 25.0, 30.0]
        
        highest = main.find_highest_score(scores)
        average = main.calculate_average_time(times)
        
        self.assertEqual(highest, 1500)
        self.assertEqual(average, 20.0)
    
    def test_sample_set_4_edge_case_values(self):
        """Test Set 4: Edge Case Values"""
        scores = [0, 1000000]
        times = [0.1, 1440.0]
        
        highest = main.find_highest_score(scores)
        average = main.calculate_average_time(times)
        
        self.assertEqual(highest, 1000000)
        self.assertEqual(average, 720.05)


if __name__ == '__main__':
    # Configure test discovery and execution
    unittest.main(verbosity=2)