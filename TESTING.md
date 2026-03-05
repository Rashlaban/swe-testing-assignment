# Testing Strategy for Quick-Calc

## What I Tested
The project uses a multi-layer test approach:
- **Unit tests** for the core calculation functions (`add`, `subtract`, `multiply`, `divide`) to ensure correct outputs for normal inputs and edge cases.
- **Integration tests** for the press-based calculator workflow (`QuickCalc.press`) to ensure user-like button sequences correctly interact with the calculation logic.

## What I Did Not Test (and Why)
- **GUI/visual interface testing**: The assignment focuses on code quality and testing, not UI.
- **Non-functional testing** such as performance, load, or security: Out of scope for a small calculator and not required by the brief.
- **Floating-point formatting perfection** for every possible decimal case: The focus is correctness of operations and basic display behavior.

## How This Relates to Lecture 3 Concepts

### 1) Testing Pyramid
This repository follows the testing pyramid:
- Many **unit tests** (fast, isolated, most coverage)
- Fewer **integration tests** (slower, higher-level, check components together)

This provides quick feedback during development while still verifying end-to-end behavior.

### 2) Black-box vs White-box Testing
- **Unit tests** are closer to **white-box** testing because they directly call internal functions and verify specific logic paths (e.g., division-by-zero raises an error).
- **Integration tests** are more **black-box** because they simulate user interactions (pressing buttons) and only assert visible outcomes (display result), without checking internal variables.

### 3) Functional vs Non-Functional Testing
- The suite focuses on **functional testing**: verifying the calculator produces correct results for supported operations and handles invalid operations like dividing by zero.
- **Non-functional testing** (performance/security/usability) was intentionally not included because it is outside the required scope.

### 4) Regression Testing
These tests support **regression testing** because after any future change (e.g., new feature or refactor), running:
`python -m pytest`
quickly confirms the existing behavior still works. If a change breaks a previous feature, the tests fail immediately.

## Test Results Summary

| Test Name | Type | Status |
|---|---|---|
| test_add_integers | Unit | Pass |
| test_subtract_integers | Unit | Pass |
| test_multiply_integers | Unit | Pass |
| test_divide_integers | Unit | Pass |
| test_divide_by_zero_raises | Unit | Pass |
| test_add_negative_numbers | Unit | Pass |
| test_multiply_decimals | Unit | Pass |
| test_large_number_addition | Unit | Pass |
| test_full_flow_addition_5_plus_3_equals_8 | Integration | Pass |
| test_clear_resets_after_calculation | Integration | Pass |