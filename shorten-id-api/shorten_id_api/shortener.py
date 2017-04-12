import math

from functools import reduce


CHARACTER_SET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE = len(CHARACTER_SET)


def encode_id(id: int) -> str:
    digits = []
    while id > 0:
        rem = id % BASE
        digits.insert(0, rem)
        id = id // BASE
    mapped = map(lambda x: CHARACTER_SET[x], digits)
    return "".join(mapped)


def decode_id(short_id: str) -> int:
    ch_list = [x for x in short_id]
    return reduce(lambda x, y: x * BASE + CHARACTER_SET.index(y), ch_list, 0)
