from __future__ import annotations

from python_template.product import main


def test_main_trivial():
    assert main(['--op1=6', '--op2=6']) == 1
    assert main(['--op1=6', '--op2=t']) == 0
