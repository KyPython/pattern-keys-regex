# Pattern Keys Regex Engine

A minimal, educational regex engine implementation in Python, built as part of a creative coding project exploring the intersection of pattern matching and worldbuilding.

## Overview

This project implements a simplified regex engine from scratch, supporting:
- **Literal character matching** (exact matches)
- **`.` wildcard** (matches any single character)
- **`*` operator** (zero or more of the preceding character/pattern)

The engine uses recursive backtracking to handle variable-length patterns and includes comprehensive test coverage.

## Features

### Core Functionality

- **`matches(pattern, text)`** — Check if text fully matches a pattern
- **`find_all_matches(pattern, text)`** — Find all matching substrings in text
- Greedy matching for `*` operator
- Full string matching (not prefix matching)
- Support for non-ASCII characters

### Example Usage

```python
from SimpleRegexMatcher import matches, find_all_matches

# Literal matching
matches("abc", "abc")  # True

# Wildcard matching
matches("a.c", "abc")  # True
matches("a.c", "axc")  # True

# Star operator (zero or more)
matches("a*b", "b")    # True (zero a's)
matches("a*b", "ab")   # True (one a)
matches("a*b", "aab")  # True (two a's)

# Universal pattern
matches(".*", "anything")  # True

# Find all matches
find_all_matches("a.c", "abc xyz abc")
# Returns: [(0, 3, 'abc'), (8, 11, 'abc')]
```

## Technical Details

### Implementation

- **Algorithm**: Recursive backtracking with greedy matching
- **Time Complexity**: O(2^n) in worst case (exponential due to backtracking)
- **Space Complexity**: O(n) for recursion stack
- **Pattern Support**: Literals, `.`, `*` (no `+`, `?`, character classes, or anchors yet)

### Test Coverage

13 comprehensive test cases covering:
- Exact literal matches
- Wildcard patterns
- Star operator (zero or more)
- Edge cases (empty strings, non-ASCII, length mismatches)
- Complex patterns with multiple `*` operators
- `find_all_matches()` functionality

Run tests:
```bash
python3 SimpleRegexMatcher.py
# or
python3 -m pytest SimpleRegexMatcher.py -v
```

## Project Structure

```
pattern-keys-regex/
├── SimpleRegexMatcher.py      # Main regex engine implementation
├── PatternKeys_Integration.md # Creative lore and integration notes
└── README.md                  # This file
```

## Pattern Keys Lore

This project is part of a creative worldbuilding exercise exploring "Pattern Keys" — forbidden codes that act as linguistic filters, unlocking hidden layers of meaning within text. The regex engine serves as the technical foundation for this concept.

See `PatternKeys_Integration.md` for:
- Technical overview
- In-world use cases
- Game/movie/book hooks
- Music direction notes

## Version History

### v1 (Current)
- Added `*` operator support with recursive backtracking
- Refactored tests into `unittest.TestCase` class
- Added `find_all_matches()` function
- Enhanced documentation and lore

### v0
- Basic literal and `.` wildcard matching
- Fixed-length pattern matching
- Simple test harness

## Future Improvements (v2)

- Support for `+` (one or more)
- Support for `?` (zero or one)
- Character classes `[a-z]`, `[0-9]`
- Anchors `^` and `$`
- Non-greedy matching `*?`
- Performance optimizations (memoization, NFA/DFA conversion)

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

This is a personal/educational project. Feel free to use and modify as needed.

## Author

Built as part of a creative coding and worldbuilding project exploring pattern matching, regex engines, and narrative design.

---

**Note**: This is a minimal, educational implementation. For production use, consider Python's built-in `re` module or more robust regex libraries.

