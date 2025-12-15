# Pattern Keys — Regex Engine Integration

## Technical Overview

This minimal regex engine (v1) implements a simplified pattern-matching system that processes text using recursive backtracking. The engine supports **literal characters** (exact matches), **`.` wildcard** (matches any single character), and the **`*` operator** (zero or more of the preceding character/pattern). Patterns and text can now have different lengths due to the `*` operator.

**Supported Features:**
- Literal character matching (e.g., `"abc"` matches `"abc"`)
- Single-character wildcard `.` (e.g., `"a.c"` matches `"abc"`, `"axc"`, `"a1c"`, etc.)
- `*` operator for zero or more repetitions (e.g., `"a*b"` matches `"b"`, `"ab"`, `"aab"`, etc.)
- `.*` matches any sequence of characters (e.g., `".*"` matches any string)
- Full string matching (entire text must match pattern)
- Empty string handling (empty pattern matches empty text)
- `find_all_matches()` function to find all matching substrings in a text

**Current Limitations (v1):**
- No other repetition operators (`+`, `?`)
- No character classes (`[a-z]`, `[0-9]`)
- No anchors (`^`, `$`)
- Greedy matching only (no non-greedy `*?`)

---

## Lore & Concept

**Pattern Keys** are forbidden codes that act as linguistic filters, unlocking hidden layers of meaning within text. In this world, certain character sequences—when processed through pattern-matching algorithms—reveal encrypted messages, activate dormant systems, or breach dimensional barriers between languages.

The `.` wildcard represents a **universal key slot**: a position where any character can unlock the pattern, suggesting that Pattern Keys are not rigid ciphers but adaptive filters that scan for structural matches rather than exact content. The `*` operator introduces **repetition gates**: a character or wildcard followed by `*` can appear zero or more times, creating variable-length patterns that can match texts of different lengths. This makes Pattern Keys even more dangerous: they can match unintended texts across multiple lengths, causing systems to activate or decrypt information when they shouldn't. The `.*` pattern is particularly feared—it matches *any* sequence, making it a master key that can unlock almost any lock.

**In-World Use Cases:**
1. **Archive Decryption**: Ancient texts contain Pattern Keys that, when matched against spoken phrases, unlock sealed knowledge repositories.
2. **Security Bypass**: Certain systems accept Pattern Keys instead of exact passwords—a single `.` in the right position can grant access if an attacker knows the pattern structure.
3. **Language Translation Gates**: Pattern Keys act as filters that detect when text matches a "template" of a forbidden language, triggering automatic translation or quarantine protocols.

---

## Game / Movie / Book Hooks

### Game Mechanic: Pattern Lock Puzzles
Players discover Pattern Keys scattered throughout the world (e.g., `"T..E"`). They must find text that matches these patterns to unlock doors, decrypt messages, or activate ancient machinery. The challenge: multiple texts might match a single pattern, so players must choose the "correct" match based on context clues. Example: Pattern `".A.."` could match `"CAGE"`, `"FATE"`, or `"WAVE"`—but only one opens the door to the next level.

### Movie Scene: The Pattern Key Breach
In a tense sequence, hackers attempt to break into a secure facility. They know the password pattern is `"ADM.N"` but not the exact characters. They try multiple combinations (`"ADMIN"`, `"ADMIN"`, `"ADM1N"`) while security systems detect the pattern-matching attempts and begin locking down. The race: can they find the right match before the system fully seals?

### Book/Lore Device: The Forbidden Lexicon
A scholar discovers that ancient texts contain Pattern Keys that, when matched against modern speech, reveal hidden meanings. The pattern `".E.."` appears in multiple prophecies. When matched against words like `"FATE"`, `"TIME"`, `"LIFE"`, it triggers visions of possible futures. The twist: the pattern itself is a trap—matching it too many times causes the scholar's own speech to become filtered, and they begin speaking only in words that match Pattern Keys, losing their ability to communicate normally.

---

## Music Direction — Pattern Keys Motif

**Mood**: Hypnotic, precise, slightly eerie. The music should feel like a scanning process—methodical and relentless, with a sense that something is being filtered or decoded in real-time.

**Musical Texture**: A repeating arpeggio pattern (perhaps in a minor key, like A minor or D minor) that cycles through the same sequence, but with subtle variations each iteration—like a pattern matcher trying different character combinations. The rhythm should be **staccato and mechanical**, evoking the character-by-character comparison process. Underneath, a low, sustained drone suggests the hidden layer of meaning being unlocked. As the pattern "matches," introduce a brief, shimmering harmonic shift (maybe a suspended chord resolving) to indicate successful decryption.

**Instrumentation Ideas**: 
- Pulsing synthesizer arpeggio (main pattern)
- Low strings or synth bass (drone)
- Metallic percussion (staccato rhythm)
- Glassy, ethereal pads (for the "match" moments)

The overall effect should be **uncanny but precise**—like watching a lock mechanism click into place, but the lock is made of language itself.

