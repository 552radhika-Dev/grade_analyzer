# Copilot Instructions

## Project Overview
This is a minimal Python project containing a simple example script. The codebase consists of a single module with basic functionality for demonstration purposes.

## Project Structure
- **test1.py**: Single entry-point script containing the `greet()` function

## Architecture & Patterns
This project follows a straightforward structure:
- Functions are executed directly at module level (see `greet()` call at end of test1.py)
- No external dependencies or complex data flows
- Direct print-based output for simple I/O

## Key Files & Conventions
- **test1.py**: Contains application logic; functions follow snake_case naming
  - `greet()`: Basic function that prints output to console
  - Module executes `greet()` on import for testing

## Development Workflow
### Running the Script
```bash
python test1.py
```
Expected output: `My name is Radhika`

### Code Style
- Use snake_case for function names
- Keep functions focused on single responsibilities
- Use print() for console output

## Future Expansion Guidance
If expanding this project:
1. Create `requirements.txt` if adding external dependencies
2. Add a `main()` function and proper if `__name__ == "__main__":` guards for larger scripts
3. Consider organizing into packages if functionality grows
4. Add type hints for clarity (Python 3.5+ style: `def greet() -> None:`)
