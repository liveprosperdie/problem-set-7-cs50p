# Pset 7 — Regular Expressions

Solutions for CS50P Week 7 problem set, focused on pattern matching using Python's `re` module and third-party validation libraries.

---

## Problems

### 1. NUMB3RS (`numb3rs.py`)

Validates IPv4 addresses inspired by a scene in the TV show *NUMB3RS* where an invalid IP (`275.3.6.28`) appears on screen.

**How it works:**
- Uses `re.search` to match four dot-separated digit groups
- Checks each octet is within the valid range `[0, 255]`
- Returns `True` for valid addresses, `False` otherwise

**Example:**
```
IPv4 Address: 275.3.6.28
False

IPv4 Address: 192.168.1.1
True
```

**Key concept:** Regex handles format, Python handles value range — two separate steps.

---

### 2. Watch on YouTube (`watch.py`)

Extracts YouTube embed URLs from HTML and converts them to shorter `youtu.be` links.

**Supported input formats:**
- `http://youtube.com/embed/VIDEO_ID`
- `https://youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

**Example:**
```
HTML: <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
https://youtu.be/xvFZjo5PgG0
```

**Returns:** `None` if no valid YouTube embed URL is found.

---

### 3. Working 9 to 5 (`working.py`)

Converts 12-hour time ranges to 24-hour format.

**Accepted input formats:**
- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`
- `9:00 AM to 5 PM`
- `9 AM to 5:00 PM`

**Example:**
```
Hours: 9 AM to 5 PM
09:00 to 17:00

Hours: 12:00 AM to 12:00 PM
00:00 to 12:00
```

**Raises:** `ValueError` for invalid formats or out-of-range times (e.g. `13:00 AM`, `9:60 PM`).

---

### 4. Um, Uh (`um.py`)

Counts how many times the word "um" appears in a string, case-insensitively. Does not count words that merely contain "um" (e.g. `yummy`, `umbrella`).

**Example:**
```
Text: Um, what do you, um, think?
2
```

**Key concept:** `\bum\b` uses word boundaries to match `um` as a standalone word only.

---

### 5. Response Validation (`response.py`)

Validates whether an input is a syntactically valid email address using the `validators` library from PyPI.

**Example:**
```
What's your email address? alice@example.com
Valid

What's your email address? notanemail
Invalid
```

**Note:** Does not verify whether the domain actually exists — only checks syntax.

---

## Tests

| File | Tests |
|---|---|
| `test_numb3rs.py` | Valid IPs, out-of-range octets, letters, extra octets |
| `test_working.py` | Valid times, edge cases (12 AM/PM), late night hours, invalid formats |
| `test_um.py` | Normal count, case sensitivity, start/end of string, non-um words |

Run all tests:
```
python -m pytest
```

---

## Key Concepts Learned

- `re.fullmatch` vs `re.search` vs `re.match`
- Capturing groups with `(\d+)` and retrieving via `.group()`
- Word boundaries with `\b`
- Optional groups with `?`
- Using `all()` for clean range validation
- `pytest.raises()` for testing exceptions
- Third-party PyPI libraries (`validators`)
