from __future__ import annotations

import argparse
from typing import Sequence


def multiply_two_nums(num1: int, num2: int) -> int:
    return num1 * num2


def main(argv: Sequence[str] | None = None) -> int:
    retv = 0
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--op1', help='The first number to be multiplied')
        parser.add_argument('--op2', help='The second number to be multiplied')
        args = parser.parse_args(argv)
        print(
            f'{args.op1}*{args.op2}='
            f'{multiply_two_nums(int(args.op1), int(args.op2))}',
        )
        retv = 1
    except ValueError:
        return retv
    return retv


if __name__ == '__main__':
    raise SystemExit(main())
