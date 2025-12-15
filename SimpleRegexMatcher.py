"""
SimpleRegexMatcher — A minimal regex engine supporting literals, '.' wildcard, and '*' operator.

This is v1 of the engine. It supports:
- Literal character matching (exact match)
- '.' wildcard (matches any single character)
- '*' operator (zero or more of the preceding character/pattern)

Constraints:
- Pattern and text can now have different lengths (due to *)
- No other repetition operators (+, ?)
- No character classes ([...])
- No anchors (^, $) — matching is position-by-position

Future v2 improvements:
- Support for + (one or more)
- Support for ? (zero or one)
- Character classes [a-z]
- Anchors ^ and $
"""

import unittest


def _match_recursive(pattern: str, text: str, pattern_idx: int, text_idx: int) -> bool:
    """
    Recursive helper function for pattern matching with backtracking.
    
    Handles:
    - Literal characters
    - '.' wildcard
    - '*' operator (zero or more of preceding)
    
    Args:
        pattern: The full pattern string
        text: The full text string
        pattern_idx: Current position in pattern
        text_idx: Current position in text
        
    Returns:
        True if text[text_idx:] matches pattern[pattern_idx:], False otherwise
    """
    # Base case: both pattern and text are exhausted
    if pattern_idx >= len(pattern) and text_idx >= len(text):
        return True
    
    # If pattern is exhausted but text remains, no match
    if pattern_idx >= len(pattern):
        return False
    
    # Check for * operator (lookahead)
    if pattern_idx + 1 < len(pattern) and pattern[pattern_idx + 1] == '*':
        # Handle * operator: zero or more of the preceding character
        char_to_match = pattern[pattern_idx]
        
        # Greedy matching: try one or more occurrences first, then zero
        # Try one or more occurrences: consume matching characters greedily
        if text_idx < len(text):
            # Check if current text character matches the pattern before *
            if char_to_match == '.' or char_to_match == text[text_idx]:
                # Consume one character and try again (stay at same pattern position for *)
                if _match_recursive(pattern, text, pattern_idx, text_idx + 1):
                    return True
        
        # Try zero occurrences: skip the 'char*' and continue
        if _match_recursive(pattern, text, pattern_idx + 2, text_idx):
            return True
        
        return False
    
    # Handle regular character or '.' (not followed by *)
    if text_idx >= len(text):
        return False
    
    char_to_match = pattern[pattern_idx]
    
    # Match single character
    if char_to_match == '.' or char_to_match == text[text_idx]:
        return _match_recursive(pattern, text, pattern_idx + 1, text_idx + 1)
    
    return False


def matches(pattern: str, text: str) -> bool:
    """
    Check if text matches pattern, supporting literals, '.', and '*' operators.
    
    Rules:
    - Literal characters must match exactly
    - '.' matches any single character
    - '*' means zero or more of the preceding character/pattern
    - Pattern and text can have different lengths (due to *)
    
    Args:
        pattern: The pattern to match against (may contain '.' and '*' operators)
        text: The text to check
        
    Returns:
        True if text matches pattern, False otherwise
        
    Examples:
        >>> matches("abc", "abc")
        True
        >>> matches("a.c", "abc")
        True
        >>> matches("a*b", "b")
        True  # Zero a's
        >>> matches("a*b", "ab")
        True  # One a
        >>> matches("a*b", "aab")
        True  # Two a's
        >>> matches(".*", "anything")
        True  # .* matches everything
        >>> matches("", "")
        True  # Empty strings match
    """
    return _match_recursive(pattern, text, 0, 0)


def find_all_matches(pattern: str, text: str) -> list[tuple[int, int, str]]:
    """
    Find all substrings of text that match the pattern.
    
    Returns a list of tuples: (start_index, end_index, matched_substring)
    where start_index is inclusive and end_index is exclusive.
    Overlapping matches are included.
    
    Args:
        pattern: The pattern to match against
        text: The text to search in
        
    Returns:
        List of (start, end, substring) tuples for all matches
        
    Examples:
        >>> find_all_matches("a.c", "abc xyz abc")
        [(0, 3, 'abc'), (8, 11, 'abc')]
        >>> find_all_matches("a*b", "aab b ab")
        [(0, 3, 'aab'), (4, 5, 'b'), (6, 8, 'ab')]
    """
    matches_list = []
    
    # Try matching pattern starting at every position in text
    for start in range(len(text) + 1):  # +1 to handle empty pattern matching empty text
        # Try matching from this start position
        # We need to check all possible end positions
        for end in range(start, len(text) + 1):
            substring = text[start:end]
            if matches(pattern, substring):
                matches_list.append((start, end, substring))
    
    return matches_list


class TestSimpleRegexMatcher(unittest.TestCase):
    """Test suite for SimpleRegexMatcher."""
    
    def test_exact_literal_matches(self):
        """Test exact literal character matching."""
        self.assertTrue(matches("abc", "abc"))
        self.assertFalse(matches("abc", "abd"))
        self.assertFalse(matches("abc", "ab"))
    
    def test_wildcard_matching(self):
        """Test '.' wildcard matching."""
        self.assertTrue(matches("a.c", "abc"))
        self.assertTrue(matches("a.c", "axc"))
        self.assertTrue(matches(".bc", "abc"))
        self.assertTrue(matches("ab.", "abc"))
        self.assertTrue(matches("...", "xyz"))
        self.assertTrue(matches(".a.", "xay"))
        self.assertFalse(matches("a.c", "ab"))
    
    def test_star_operator_zero_or_more(self):
        """Test '*' operator (zero or more)."""
        # Zero occurrences
        self.assertTrue(matches("a*b", "b"))
        self.assertTrue(matches("a*b", "ab"))
        self.assertTrue(matches("a*b", "aab"))
        self.assertTrue(matches("a*b", "aaab"))
        
        # With wildcard
        self.assertTrue(matches(".*", ""))
        self.assertTrue(matches(".*", "a"))
        self.assertTrue(matches(".*", "abc"))
        self.assertTrue(matches(".*", "anything at all"))
        
        # Complex patterns
        self.assertTrue(matches("a*b*c", "c"))
        self.assertTrue(matches("a*b*c", "bc"))
        self.assertTrue(matches("a*b*c", "abc"))
        self.assertTrue(matches("a*b*c", "aabbc"))  # Full match: aabbc (not aabbcc)
        self.assertFalse(matches("a*b*c", "aabbcc"))  # Extra 'c' at end doesn't match
        
        # Edge cases
        self.assertTrue(matches("a*", ""))
        self.assertTrue(matches("a*", "a"))
        self.assertTrue(matches("a*", "aa"))
        self.assertTrue(matches(".*", "xyz"))
    
    def test_star_operator_failures(self):
        """Test cases where '*' patterns should not match."""
        self.assertFalse(matches("a*b", "c"))
        self.assertFalse(matches("a*b", "ac"))
        self.assertFalse(matches("a*", "b"))
    
    def test_empty_strings(self):
        """Test empty string edge cases."""
        self.assertTrue(matches("", ""))
        self.assertFalse(matches("", "abc"))
        self.assertFalse(matches("abc", ""))
        self.assertTrue(matches("a*", ""))  # Zero a's matches empty
    
    def test_length_mismatches_without_star(self):
        """Test that patterns without * still require length match."""
        self.assertFalse(matches("abc", "ab"))
        self.assertFalse(matches("ab", "abc"))
    
    def test_non_ascii_characters(self):
        """Test non-ASCII character handling."""
        self.assertTrue(matches("café", "café"))
        self.assertTrue(matches("caf.", "café"))
        self.assertFalse(matches("café", "cafe"))
        self.assertTrue(matches("café*", "caf"))  # Zero é's
        self.assertTrue(matches("café*", "café"))  # One é
        self.assertTrue(matches("café*", "caféé"))  # Two é's
        self.assertFalse(matches("café*", "cafécafé"))  # café* means zero or more é, not café
    
    def test_single_character_patterns(self):
        """Test single character patterns."""
        self.assertTrue(matches(".", "a"))
        self.assertTrue(matches("a", "a"))
        self.assertFalse(matches("a", "b"))
        self.assertTrue(matches("a*", ""))
        self.assertTrue(matches("a*", "a"))
    
    def test_complex_star_patterns(self):
        """Test complex patterns with multiple * operators."""
        self.assertTrue(matches("a*b*c*", ""))
        self.assertTrue(matches("a*b*c*", "abc"))
        self.assertTrue(matches("a*b*c*", "aabbcc"))
        self.assertTrue(matches(".*.*", "xy"))
        self.assertTrue(matches(".*.*", "xyz"))
    
    def test_find_all_matches_basic(self):
        """Test find_all_matches with basic patterns."""
        results = find_all_matches("a.c", "abc xyz abc")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], (0, 3, "abc"))
        self.assertEqual(results[1], (8, 11, "abc"))
    
    def test_find_all_matches_with_star(self):
        """Test find_all_matches with * operator."""
        results = find_all_matches("a*b", "aab b ab")
        # Should find: "aab" at (0,3), "b" at (4,5), "ab" at (6,8)
        self.assertGreaterEqual(len(results), 3)
        # Check that expected matches are present
        match_strings = [m[2] for m in results]
        self.assertIn("aab", match_strings)
        self.assertIn("b", match_strings)
        self.assertIn("ab", match_strings)
    
    def test_find_all_matches_empty_pattern(self):
        """Test find_all_matches with empty pattern."""
        results = find_all_matches("", "abc")
        # Empty pattern matches empty string at every position
        self.assertGreater(len(results), 0)
        # Should match at positions 0, 1, 2, 3
        self.assertEqual(len(results), 4)
    
    def test_find_all_matches_overlapping(self):
        """Test that find_all_matches finds overlapping matches."""
        results = find_all_matches(".*", "abc")
        # .* matches everything, so should find matches at multiple positions
        self.assertGreater(len(results), 1)


if __name__ == "__main__":
    # Run unittest test suite
    unittest.main(verbosity=2)
