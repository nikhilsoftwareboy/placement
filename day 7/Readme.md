# remove_html_chars.py Documentation

## Overview
This module provides utility functions for removing and manipulating characters from strings, with a primary focus on HTML character removal.

## Functions

### 1. `help_menu()`
Displays a help menu with information about the available methods in the package.

**Parameters:**
- None

**Returns:**
- None (prints to console)

**Description:**
Prints a help menu indicating that the package has 3 methods available. Also displays the docstring of the function itself.

**Example:**
```python
help_menu()
# Output: Prints help menu information to console
```

---

### 2. `remove_html_chars(html_input: str) -> str`
Removes HTML-specific characters from a given string.

**Parameters:**
- `html_input` (str): The input string containing HTML characters to be removed

**Returns:**
- str: The string with HTML characters (`<`, `>`, `/`) removed

**Description:**
This function removes three specific HTML-related characters from the input string:
- `<` (less than sign)
- `>` (greater than sign)
- `/` (forward slash)

These characters are common in HTML tags and attributes.

**Example:**
```python
result = remove_html_chars("<div>Hello</div>")
# result would be "divHellodiv"
```

---

### 3. `remove_char(input_string, rem_ove)`
Removes a specified character from a string and prints the result.

**Parameters:**
- `input_string` (str): The input string from which to remove the character
- `rem_ove` (str): The character or substring to be removed

**Returns:**
- None (prints the result to console)

**Description:**
This function takes a string and a character/substring to remove, then prints the resulting string with all occurrences of the specified character removed.

**Example:**
```python
remove_char("Hello World", "o")
# Output: Hll Wrld
```

---

## Usage Notes
- The `remove_html_chars()` function currently does not return the modified string (missing return statement in the code)
- The `remove_char()` function prints the result but does not return it
- These functions are part of a larger package designed for string manipulation

## Dependencies
- Python 3.x (uses type hints)
