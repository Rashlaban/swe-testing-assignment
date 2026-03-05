# Quick-Calc

Quick-Calc is a simple calculator application that supports addition, subtraction, multiplication, division (with safe handling of division by zero), and a clear (C) function that resets the current input and result back to zero.

The focus of this project is clean, testable code and a multi-layer testing strategy using Git and GitHub.

## Project Structure

- `quick_calc/core.py` — core calculation logic (pure functions)
- `quick_calc/app.py` — press-based calculator workflow (input layer)
- `tests/unit/` — unit tests for core logic
- `tests/integration/` — integration tests for full user-like flows

## Setup Instructions (Windows)

1. Clone the repository:
   ```powershell
   git clone https://github.com/<your-username>/swe-testing-assignment.git
   cd swe-testing-assignment

2. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\Activate.ps1

3. Install dependencies:

pip install -r requirements.txt
Run the Application

This project is intentionally lightweight and focuses on testability rather than a full UI. The calculator behavior can be used through the QuickCalc class.

## Example (interactive):

4. Start Python:

python

Run this code:

from quick_calc.app import QuickCalc

c = QuickCalc()
c.press("5")
c.press("+")
c.press("3")
c.press("=")
print(c.display)  # 8

c.press("C")
print(c.display)  # 0

## How to Run Tests

5. Run the full suite from the repository root:

python -m pytest

6. Testing Framework Research: Pytest vs Unittest

Python includes unittest as a built-in testing framework based on the xUnit style. Its main advantage is that it ships with Python, so it requires no extra installation and is commonly used in many existing codebases. However, unittest often leads to more boilerplate because tests are typically written inside classes, use specific method naming conventions, and rely on framework-specific assertion methods. For small projects, this can make tests longer and less readable.

pytest is a popular third-party framework that emphasizes simplicity and developer productivity. It allows writing tests as plain functions, provides powerful features such as fixtures and parameterization, and offers very clear failure output through assertion introspection (helpful error messages showing exactly what failed). This typically results in cleaner tests that are easier to extend as the project grows.

For Quick-Calc, pytest was chosen because it reduces boilerplate, makes it fast to write many unit tests, and supports integration tests cleanly. The concise syntax and helpful failure messages make it well suited for using the test suite as regression protection when adding new features or refactoring.