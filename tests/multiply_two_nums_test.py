from __future__ import annotations

from python_template.product import multiply_two_nums


def test_multiplication():
    assert multiply_two_nums(3, 3) == 9
    assert multiply_two_nums(0, 0) == 0
    assert multiply_two_nums(-1, 6) == -6
    assert multiply_two_nums(-1, -1) == 1
