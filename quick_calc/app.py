# quick_calc/app.py
from __future__ import annotations

from quick_calc.core import add, subtract, multiply, divide, DivisionByZeroError


class QuickCalc:
    """
    Simple press-based calculator to support integration testing.

    Buttons supported:
    - digits: "0".."9"
    - decimal point: "."
    - operators: "+", "-", "*", "/"
    - equals: "="
    - clear: "C"
    """
    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.display = "0"
        self._stored_value: float | None = None
        self._pending_op: str | None = None
        self._new_number = True  # next digit starts a new number

    def press(self, key: str) -> str:
        if key == "C":
            self.clear()
            return self.display

        if key in "0123456789":
            return self._press_digit(key)

        if key == ".":
            return self._press_decimal()

        if key in {"+", "-", "*", "/"}:
            return self._press_operator(key)

        if key == "=":
            return self._press_equals()

        raise ValueError(f"Unsupported key: {key}")

    def _press_digit(self, digit: str) -> str:
        if self._new_number:
            self.display = digit
            self._new_number = False
        else:
            if self.display == "0":
                self.display = digit
            else:
                self.display += digit
        return self.display

    def _press_decimal(self) -> str:
        if self._new_number:
            self.display = "0."
            self._new_number = False
            return self.display

        if "." not in self.display:
            self.display += "."
        return self.display

    def _press_operator(self, op: str) -> str:
        if self._pending_op is not None and self._stored_value is not None and not self._new_number:
            self._evaluate()

        self._stored_value = float(self.display)
        self._pending_op = op
        self._new_number = True
        return self.display

    def _press_equals(self) -> str:
        if self._pending_op is None or self._stored_value is None:
            return self.display

        self._evaluate()
        self._pending_op = None
        self._stored_value = None
        self._new_number = True
        return self.display

    def _evaluate(self) -> None:
        assert self._stored_value is not None
        current = float(self.display)

        try:
            if self._pending_op == "+":
                result = add(self._stored_value, current)
            elif self._pending_op == "-":
                result = subtract(self._stored_value, current)
            elif self._pending_op == "*":
                result = multiply(self._stored_value, current)
            elif self._pending_op == "/":
                result = divide(self._stored_value, current)
            else:
                raise ValueError("No pending operation.")
        except DivisionByZeroError:
            self.display = "Error"
            self._stored_value = None
            self._pending_op = None
            self._new_number = True
            return

        if result == int(result):
            self.display = str(int(result))
        else:
            self.display = str(result)