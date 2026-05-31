# Reverse Polish Notation (RPN) Calculator

A clean Python implementation of the **Shunting-yard algorithm** and **RPN evaluation**. It automatically converts standard mathematical infix expressions into RPN tokens and calculates the exact final result.

## Key Features
- **Smart Tokenization**: Automatically groups characters into multi-digit numbers (e.g., `10` or `135`) without forcing the user to type spaces.
- **Advanced Priorities**: Supports core operators `+`, `-`, `*`, `/` alongside High-priority Modulo (`M`) and Power (`^`).
- **Parentheses Support**: Correctly processes `()` to dynamically change the order of operations.

## Test Case Examples

### Example 1:
- **Input**: `12-5*35M4^2+0`
- **RPN Output**: `['12', '5', '35', '4', '2', '^', 'M', '*', '-', '0', '+']`
- **Final Result**: `-3`

### Example 2:
- **Input**: `2+(2/4*(12M5)^3)-0` or `2 + ( 2 / 4 * ( 12 M 5 ) ^ 3 ) - 0`
- **RPN Output**: `['2', '2', '4', '/', '12', '5', 'M', '3', '^', '*', '+', '0', '-']`
- **Final Result**: `2`
