import unittest
from Match import Match


class PatternMatchTest(unittest.TestCase):
    def test_regular_matching_in_between(self):
        pattern = 'cat'
        target_string = 'acatb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(1, startIndex)

    def test_regular_matching_first_position(self):
        pattern = 'cat'
        target_string = 'catb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(0, startIndex)

    def test_regular_not_matching(self):
        pattern = 'act'
        target_string = 'catb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(-1, startIndex)

    def test_dot_match_in_between_character(self):
        pattern = 'a.t'
        target_string = 'catb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(-1, startIndex)

    def test_dot_match_start_character(self):
        pattern = '.at'
        target_string = 'catb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(0, startIndex)

    def test_dot_match_end_character(self):
        pattern = 'cat.'
        target_string = 'acatb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(1, startIndex)

    def test_empty(self):
        pattern = ''
        target_string = ''
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(-1, startIndex)

    def test_empty_star_pattern(self):
        pattern = '*'
        target_string = ''
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(-1, startIndex)

    def test_star_match_starting_characters(self):
        pattern = '*at'
        target_string = 'bobcat'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(0, startIndex)

    def test_star_match_zero_characters(self):
        pattern = 'c*t'
        target_string = 'bobct'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(3, startIndex)

    def test_star_match_ending_characters(self):
        pattern = 'a*'
        target_string = 'ca'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(1, startIndex)

    def test_star(self):
        pattern = 'ca*'
        target_string = 'bobcat'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(3, startIndex)

    def test_star_longer_string(self):
        pattern = 'c*tb'
        target_string = 'bobcatatb'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(3, startIndex)

    def test_star_dot(self):
        pattern = 'c*.t'
        target_string = 'bobcat'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(3, startIndex)

    def test_non_alpha_characters(self):
        pattern = 'c?!t'
        target_string = 'bobcat'
        match = Match(pattern)
        startIndex = match.find_first_in(target_string)
        self.assertEqual(-1, startIndex)


if __name__ == '__main__':
    unittest.main()
